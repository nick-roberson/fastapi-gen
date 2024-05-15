import copy
import json
import os
import subprocess
import tempfile
import time
from typing import Dict, List, Tuple

import pytest
import requests

from builder.config.parse import load_and_validate_config
from builder.generate.backend.generator import BackendGenerator
from builder.generate.poetry.generator import PoetryGenerator
from builder.managers.db.manager import DBManager
from builder.managers.linting.manager import LintingManager
from builder.models.configs import ServiceConfig
from builder.test_data.create_fake_data import create_fake_data

# Constants for the service's endpoint details
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
BASE_URL = f"http://{DEFAULT_HOST}:{DEFAULT_PORT}"
NUM_MODELS = 5  # Number of model instances for testing

# Load configurations
TEST_RESTAURANTS_CONFIG_FP = os.path.abspath("builder/tests/configs/restaurant.yaml")
TEST_RESTAURANT_CONFIG: ServiceConfig = load_and_validate_config(
    TEST_RESTAURANTS_CONFIG_FP
)

# Prepare model endpoint parameters
TEST_RESTAURANT_PARAMS = [
    (model.name, model.name.lower() + "s") for model in TEST_RESTAURANT_CONFIG.models
]


# Helper functions
def _get_models(model_name: str) -> List[Dict]:
    """Get all models from the given endpoint"""
    url = f"{BASE_URL}/{model_name.lower()}s"
    print(f"[_get_models] Getting models from {url}")
    response = requests.get(url)
    response.raise_for_status()
    assert response.status_code == 200
    return response.json()


def _get_model(model_name: str, model_id: int) -> Dict:
    """Get a model instance with the given ID"""
    url = f"{BASE_URL}/{model_name.lower()}"
    print(f"[_get_model] Getting model {url}: {model_id}")
    params = {f"{model_name.lower()}_id": model_id}
    response = requests.get(url, params=params)
    response.raise_for_status()
    assert response.status_code == 200
    return response.json()


def _create_model(model_name: str, model_data: Dict) -> Dict:
    """Create a model instance using the given data"""
    url = f"{BASE_URL}/{model_name.lower()}"
    print(f"[_create_model] Creating model with data {url}: {model_data}")
    response = requests.post(url, json=model_data)
    response.raise_for_status()
    assert response.status_code == 200
    return response.json()


def _delete_model(model_name: str, model_id: int) -> Dict:
    """Delete a model instance with the given ID"""
    url = f"{BASE_URL}/{model_name.lower()}"
    print(f"[_delete_model] Deleting model {url}: {model_id}")
    params = {f"{model_name.lower()}_id": model_id}
    response = requests.delete(url, params=params)
    response.raise_for_status()
    assert response.status_code == 200
    return response.json()


def _query_models(model_name: str, query: Dict) -> List[Dict]:
    """Query models using the given query"""
    url = f"{BASE_URL}/{model_name.lower()}/query"
    print(f"[_query_models] Querying models {url}: {query}")
    response = requests.post(url, json=query)
    response.raise_for_status()
    assert response.status_code == 200
    return response.json()


def _update_model(model_name: str, model_id: int, model_data: Dict) -> Dict:
    """Update a model instance with the given ID"""
    url = f"{BASE_URL}/{model_name.lower()}"
    print(f"[_update_model] Updating model {url}: {model_id} with data: {model_data}")
    params = {f"{model_name.lower()}_id": model_id}
    response = requests.put(url, params=params, json=model_data)
    response.raise_for_status()
    assert response.status_code == 200
    return response.json()


# Fixtures
@pytest.fixture(scope="module")
def service():
    with tempfile.TemporaryDirectory() as output_dir:
        config = copy.copy(TEST_RESTAURANT_CONFIG)
        config.output_dir = output_dir

        # Generate and set up the backend service
        generator = BackendGenerator(config=config)
        generator.generate_models()
        generator.generate_services()
        generator.generate_templated_components()
        generator.generate_database()
        generator.generate_readme()

        linting_manager = LintingManager(config=config)
        linting_manager.lint_backend()

        poetry_generator = PoetryGenerator(config=config)
        poetry_generator.generate_poetry_toml()
        poetry_generator.install_dependencies()

        db_manager = DBManager(config=config)
        db_manager.create_migration("Initial migration")
        db_manager.run_migrations()
        db_manager.show_migrations()

        # Start the service
        service_dir = os.path.join(output_dir, "backend")
        proc = subprocess.Popen(
            [
                "uvicorn",
                "service:app",
                "--host",
                DEFAULT_HOST,
                "--port",
                str(DEFAULT_PORT),
                "--reload",
            ],
            cwd=service_dir,
        )
        time.sleep(5)  # Allow time for the server to start
        yield proc, output_dir
        proc.kill()
        proc.wait()


@pytest.fixture(scope="module")
def fake_data(service):
    proc, output_dir = service
    fake_data_paths = create_fake_data(
        config=TEST_RESTAURANT_CONFIG, num=NUM_MODELS, no_ids=True
    )

    fake_data = {}
    for model_name, fake_data_path in fake_data_paths.items():
        with open(fake_data_path, "r") as f:
            data = json.load(f)
            fake_data[model_name] = data
    yield fake_data


# Tests
@pytest.mark.parametrize("model_name, endpoint", TEST_RESTAURANT_PARAMS)
def test_create_and_manage_models(
    service: Tuple, fake_data: Dict, model_name, endpoint: str
):
    proc, output_dir = service

    # Get the fake data for the model and check it
    model_data = fake_data[model_name]
    assert model_data
    assert len(model_data) == NUM_MODELS

    # Test model creation and listing
    created_instances = []
    for data in model_data:
        created_instance = _create_model(model_name, data)
        created_instances.append(created_instance["id"])

    # Check that all models were created
    all_models = _get_models(model_name)
    assert len(all_models) == NUM_MODELS

    # Check that we can query each model instance, update it, and check the updated data
    for created_id in created_instances:

        # Get the model instance and check its data
        query = {"id": created_id}
        queried_models = _query_models(model_name, query)
        assert len(queried_models) == 1

        # Update all string fields to check if the update works
        model_instance = queried_models[0]
        updated_data = {
            key: f"{value}_updated"
            for key, value in model_instance.items()
            if isinstance(value, str) and key != "id"
        }
        updated_instance = _update_model(model_name, created_id, updated_data)

        # Check that the updated data is correct
        assert updated_instance["id"] == created_id
        for key, value in updated_data.items():
            if isinstance(value, str):
                assert updated_instance[key] == value

    # Test model deletion
    for model_id in created_instances:

        # Delete the model and check if it was removed
        deleted_model = _delete_model(model_name, model_id)
        assert deleted_model["id"] == model_id

        # Check that fetching this model now raises an error
        with pytest.raises(requests.HTTPError):
            _get_model(model_name, model_id)

    # Check that getting all models will raise an error
    with pytest.raises(requests.HTTPError):
        _get_models(model_name)
