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
from builder.generate.linting.manager import LintingManager
from builder.generate.poetry.generator import PoetryGenerator
from builder.models.configs import ServiceConfig
from builder.test_data.create_fake_data import create_fake_data

# Constants to store the default host, port, and base URL of the running service
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
BASE_URL = f"http://{DEFAULT_HOST}:{DEFAULT_PORT}"
NUM_MODELS = 5

# Constants to store the config and parameters for the tests
TEST_RESTAURANTS_CONFIG_FP: str = os.path.abspath(
    "builder/tests/configs/restaurant.yaml"
)
TEST_EVENTS_CONFIG_FP: str = os.path.abspath("builder/tests/configs/events.yaml")

# Load and validate the restaurant config
TEST_RESTAURANT_CONFIG: ServiceConfig = load_and_validate_config(
    TEST_RESTAURANTS_CONFIG_FP
)
TEST_RESTAURANT_PARAMS: List[Tuple] = [
    (model.name, model.name.lower()) for model in TEST_RESTAURANT_CONFIG.models
]


# Fixture to create the code and start the service
@pytest.fixture(scope="module")
def service():
    """Fixture to create the code and start the service, and ensure cleanup after tests."""
    # Create a temporary directory that will be cleaned up automatically
    with tempfile.TemporaryDirectory() as output_dir:
        print(f"Output directory: {output_dir}")
        # Init the backend generator
        generator = BackendGenerator(
            config=TEST_RESTAURANT_CONFIG, output_dir=output_dir
        )

        # Generate the backend code
        generator.generate_models()
        generator.generate_services()
        generator.generate_templated_components()
        generator.generate_database()
        generator.generate_readme()

        # Lint
        linting_manager = LintingManager(
            config=TEST_RESTAURANT_CONFIG, output_dir=output_dir
        )
        linting_manager.lint_backend()

        # Init the poetry generator
        poetry_generator = PoetryGenerator(
            config=TEST_RESTAURANT_CONFIG, output_dir=output_dir
        )

        # Generate the poetry code
        poetry_generator.generate_poetry_toml()
        poetry_generator.install_dependencies()

        # Start the FastAPI app with Uvicorn in a subprocess
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

        # Give Uvicorn a moment to start
        time.sleep(5)

        # Generate the Alembic migrations in the database
        db_dir = os.path.join(service_dir, "src/db")
        print("Generating Alembic migrations...")
        subprocess.run(
            ["alembic", "revision", "--autogenerate", "-m", "Initial migration"],
            cwd=db_dir,
        )

        # Run Alembic migrations
        print("Running Alembic migrations...")
        subprocess.run(
            ["alembic", "upgrade", "head"],
            cwd=db_dir,
        )

        # Yield the process and output directory to the test function
        yield proc, output_dir

        # Cleanup after the test runs
        print("Terminating the Uvicorn server...")
        proc.kill()
        proc.wait()
        print(f"Deleted output directory: {output_dir}")


@pytest.fixture(scope="module")
def fake_data(service: Tuple) -> Dict:
    """Fixture to create the fake data for the service."""
    # Unpack the service tuple
    proc, output_dir = service

    # Create the fake data
    fake_data_paths = create_fake_data(
        service_config=TEST_RESTAURANT_CONFIG,
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


def test_root_endpoints(service: Tuple):
    """Simple test to validate the example config and check the health endpoint."""
    # Unpack the service tuple
    proc, output_dir = service

    # Check the health endpoint
    BASE_URL = f"http://{DEFAULT_HOST}:{DEFAULT_PORT}"
    print(f"Running Uvicorn on {BASE_URL} and hitting the health endpoint...")

    # Perform HTTP GET request to the health endpoint
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"message": "Healthy"}

    # Perform HTTP GET request to the ready endpoint
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
