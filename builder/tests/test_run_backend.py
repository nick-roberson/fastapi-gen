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
from builder.models.configs import ServiceConfig
from builder.test_data.create_fake_data import create_fake_data

# Constants for default service parameters
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
BASE_URL = f"http://{DEFAULT_HOST}:{DEFAULT_PORT}"
NUM_MODELS = 5

# Paths to configuration files
TEST_RESTAURANTS_CONFIG_FP: str = os.path.abspath(
    "builder/tests/configs/restaurant.yaml"
)
TEST_EVENTS_CONFIG_FP: str = os.path.abspath("builder/tests/configs/events.yaml")

# Load and validate configurations
TEST_RESTAURANT_CONFIG: ServiceConfig = load_and_validate_config(
    TEST_RESTAURANTS_CONFIG_FP
)
TEST_EVENTS_CONFIG: ServiceConfig = load_and_validate_config(TEST_EVENTS_CONFIG_FP)

# Generate parameters for both configurations
TEST_RESTAURANT_PARAMS: List[Tuple] = [
    (model.name, model.name.lower(), TEST_RESTAURANT_CONFIG)
    for model in TEST_RESTAURANT_CONFIG.models
]
TEST_EVENTS_PARAMS: List[Tuple] = [
    (model.name, model.name.lower(), TEST_EVENTS_CONFIG)
    for model in TEST_EVENTS_CONFIG.models
]

# Combine parameters for parameterized tests
ALL_TEST_PARAMS = TEST_RESTAURANT_PARAMS + TEST_EVENTS_PARAMS


@pytest.fixture(scope="module")
def service(request):
    """Fixture to create and manage the service based on the configuration passed via test parameters."""
    # Get the configuration from test parameters
    print(f"Test parameters: {request}")
    config = request.param[2]

    # Create and configure service
    with tempfile.TemporaryDirectory() as output_dir:
        print(f"Output directory: {output_dir}")
        generator = BackendGenerator(config=config, output_dir=output_dir)
        generator.generate_models()
        generator.generate_services()
        generator.generate_templated_components()
        generator.generate_database()
        generator.generate_readme()
        generator.lint_backend()

        poetry_generator = PoetryGenerator(config=config, output_dir=output_dir)
        poetry_generator.generate_poetry_toml()
        poetry_generator.install_dependencies()

        service_dir = os.path.join(output_dir, "backend")
        print(f"Starting FastAPI app with Uvicorn from dir {service_dir}...")
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
        time.sleep(5)

        db_dir = os.path.join(service_dir, "src/db")
        print("Generating Alembic migrations...")
        subprocess.run(
            ["alembic", "revision", "--autogenerate", "-m", "Initial migration"],
            cwd=db_dir,
        )
        print("Running Alembic migrations...")
        subprocess.run(["alembic", "upgrade", "head"], cwd=db_dir)

        yield proc, output_dir, config

        print("Terminating the Uvicorn server...")
        proc.kill()
        proc.wait()
        print(f"Deleted output directory: {output_dir}")


@pytest.fixture(scope="module")
@pytest.fixture(scope="module")
def fake_data(service: Tuple) -> Dict:
    """Fixture to create the fake data for the service, adjusted to match the configuration in use."""
    # Unpack the service tuple
    proc, output_dir, config = (
        service  # Assuming you also yield 'config' from the 'service' fixture
    )

    # Create the fake data
    fake_data_paths = create_fake_data(
        service_config=config,
        output_dir=output_dir,
        num=NUM_MODELS,
        no_ids=True,
    )

    # Load fake data from files
    fake_data = {}
    for model_name, fake_data_path in fake_data_paths.items():
        with open(fake_data_path, "r") as f:
            data = json.load(f)
            fake_data[model_name] = data
    yield fake_data


@pytest.mark.parametrize(
    "model, endpoint, config", ALL_TEST_PARAMS, indirect=["service"]
)
def test_create_and_manage_models(
    service: Tuple, fake_data: Dict, model: str, endpoint: str, config: ServiceConfig
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
