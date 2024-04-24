import json
import os
import subprocess
import tempfile
import time
from typing import Dict, Tuple

import pytest
import requests

from builder.config.parse import load_config, parse_config
from builder.constants import TEST_MYSQL_CONFIG
from builder.generate.backend.generator import BackendGenerator
from builder.generate.poetry.generator import PoetryGenerator
from builder.test_data.create_fake_data import create_fake_data

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
BASE_URL = f"http://{DEFAULT_HOST}:{DEFAULT_PORT}"
NUM_MODELS = 5


# Fixture to create the code and start the service
@pytest.fixture(scope="module")
def service():
    """Fixture to create the code and start the service, and ensure cleanup after tests."""
    # Create a temporary directory that will be cleaned up automatically
    with tempfile.TemporaryDirectory() as output_dir:
        print(f"Output directory: {output_dir}")
        # Parse the model definitions
        config_def = load_config(TEST_MYSQL_CONFIG)
        config = parse_config(config_def)

        # Init the backend generator
        generator = BackendGenerator(config=config, output_dir=output_dir)

        # Generate the backend code
        generator.generate_models()
        generator.generate_services()
        generator.generate_templated_components()
        generator.generate_database()
        generator.generate_readme()
        generator.lint_backend()

        # Init the poetry generator
        poetry_generator = PoetryGenerator(config=config, output_dir=output_dir)

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

        # Generate the Alembic migrations
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

    # Parse the model definitions
    config_def = load_config(TEST_MYSQL_CONFIG)
    config = parse_config(config_def)

    # Create the fake data
    fake_data_paths = create_fake_data(
        service_config=config, output_dir=output_dir, num=NUM_MODELS, no_ids=True
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


def test_create_users(service: Tuple, fake_data: Dict):
    """Simple test to validate the example config and check the health endpoint."""
    # Unpack the service tuple
    proc, output_dir = service

    user_data = fake_data["User"]
    assert user_data
    assert len(user_data) == NUM_MODELS

    # Check the health endpoint
    print(f"Running Uvicorn on {BASE_URL} and hitting the health endpoint...")

    # Create one
    first_user = user_data[0]
    response = requests.post(f"{BASE_URL}/user", json=first_user)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["id"]

    # Create many
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    assert response.status_code == 200
    response_json = response.json()
    assert len(response_json) == NUM_MODELS
