import os
import subprocess
import tempfile
import time
from typing import Tuple

import pytest
import requests

from builder.config.parse import load_config, parse_config
from builder.constants import TEST_MYSQL_CONFIG
from builder.generate.backend.generator import BackendGenerator

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000


# Fixture to create the code and start the service
@pytest.fixture
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


def test_root_endpoints(service: Tuple):
    """Simple test to validate the example config and check the health endpoint."""
    # Unpack the service tuple
    proc, output_dir = service

    # Check the health endpoint
    base_url = f"http://{DEFAULT_HOST}:{DEFAULT_PORT}"
    print(f"Running Uvicorn on {base_url} and hitting the health endpoint...")
    try:
        # Give Uvicorn a moment to start
        time.sleep(3)  # Adjust sleep time if necessary

        # Perform HTTP GET request to the health endpoint
        response = requests.get(f"{base_url}/health")
        assert response.status_code == 200
        assert response.json() == {"message": "Healthy"}

        # Perform HTTP GET request to the ready endpoint
        response = requests.get(f"{base_url}/ready")
        assert response.status_code == 200
        assert response.json() == {"message": "Ready"}

        # Test single post to /user endpoint to create a user
        json = {
            "name": "John Doe",
            "email": "test@test.com",
            "phone_numer": "123-456-7890",
            "preferences": ["vegan", "gluten-free"],
            "role": "admin",
        }
        response = requests.post(f"{base_url}/user", json=json)
        assert response.status_code == 200

    # Handle any exceptions
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
