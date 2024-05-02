import copy
import json
import os
import subprocess
import tempfile
import time
from typing import Dict, Tuple

import pytest
import requests

from builder.config.parse import load_and_validate_config
from builder.generate.backend.generator import BackendGenerator
from builder.generate.db.manager import DBManager
from builder.generate.linting.manager import LintingManager
from builder.generate.poetry.generator import PoetryGenerator
from builder.models.configs import ServiceConfig
from builder.test_data.create_fake_data import create_fake_data

# Set default values for the service's host, port, and URL
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
BASE_URL = f"http://{DEFAULT_HOST}:{DEFAULT_PORT}"
NUM_MODELS = 5  # Number of model instances for testing

# Load configurations from files
TEST_RESTAURANTS_CONFIG_FP = os.path.abspath("builder/tests/configs/restaurant.yaml")
TEST_RESTAURANT_CONFIG: ServiceConfig = load_and_validate_config(
    TEST_RESTAURANTS_CONFIG_FP
)

# Prepare parameters for model tests based on configurations
TEST_RESTAURANT_PARAMS = [
    (model.name, model.name.lower()) for model in TEST_RESTAURANT_CONFIG.models
]


@pytest.fixture(scope="module")
def service():
    """Setup the application environment, start the service, and perform cleanup."""
    with tempfile.TemporaryDirectory() as output_dir:
        config = copy.copy(TEST_RESTAURANT_CONFIG)
        config.output_dir = output_dir

        # Generate backend code components and setup the environment
        generator = BackendGenerator(config=config)
        generator.generate_models()
        generator.generate_services()
        generator.generate_templated_components()
        generator.generate_database()
        generator.generate_readme()

        # Lint the generated code
        linting_manager = LintingManager(config=config)
        linting_manager.lint_backend()

        # Install project dependencies using Poetry
        poetry_generator = PoetryGenerator(config=config)
        poetry_generator.generate_poetry_toml()
        poetry_generator.install_dependencies()

        # Manage database migrations
        db_manager = DBManager(config=config)
        db_manager.create_migration("Initial migration")
        db_manager.run_migrations()
        db_manager.show_migrations()

        # Start the application server
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

        # Terminate the server and cleanup
        proc.kill()
        proc.wait()


@pytest.fixture(scope="module")
def fake_data(service):
    """Generate and load fake data for use in tests."""
    proc, output_dir = service
    fake_data_paths = create_fake_data(
        config=TEST_RESTAURANT_CONFIG, num=NUM_MODELS, no_ids=True
    )

    # Load the generated fake data from files
    fake_data = {}
    for model_name, fake_data_path in fake_data_paths.items():
        with open(fake_data_path, "r") as f:
            data = json.load(f)
            fake_data[model_name] = data
    yield fake_data


def test_root_endpoints(service):
    """Test the health and readiness endpoints of the service."""
    proc, output_dir = service

    # Test health endpoint
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"message": "Healthy"}

    # Test ready endpoint
    response = requests.get(f"{BASE_URL}/ready")
    assert response.status_code == 200
    assert response.json() == {"message": "Ready"}


# Parameterize this test to run for different model types and endpoints
@pytest.mark.parametrize(
    "model, endpoint",
    TEST_RESTAURANT_PARAMS,
)
def test_create_and_manage_models(
    service: Tuple, fake_data: Dict, model: str, endpoint: str
):
    """Test the creation, deletion, and listing of model instances."""
    # Unpack the service tuple
    proc, output_dir = service

    model_data = fake_data[model]
    assert model_data
    assert len(model_data) == NUM_MODELS

    # Create one
    first_instance = model_data[0]
    response = requests.post(f"{BASE_URL}/{endpoint}", json=first_instance)
    if response.status_code != 200:
        print(f"Failed to create {first_instance} with response: {response.text}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["id"]

    # Create many
    multiple_instances = model_data[1:5]
    response = requests.post(f"{BASE_URL}/{endpoint}s", json=multiple_instances)
    assert response.status_code == 200
    response_json = response.json()
    assert len(response_json) == 4
    assert all("id" in instance and instance["id"] for instance in response_json)

    # Query for all instances and check the count
    response = requests.get(f"{BASE_URL}/{endpoint}s")
    assert response.status_code == 200
    response_json = response.json()
    assert len(response_json) == 5

    # Delete one
    params = {
        f"{model.lower()}_id": response_json[0]["id"],
    }
    print(f"Deleting {model} with params: {params}")
    response = requests.delete(f"{BASE_URL}/{endpoint}/", params=params)
    assert response.status_code == 200

    # Query for all instances and check the count
    response = requests.get(f"{BASE_URL}/{endpoint}s")
    assert response.status_code == 200
    response_json = response.json()
    assert len(response_json) == 4
