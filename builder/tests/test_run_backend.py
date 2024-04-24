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
    """Fixture to create the code and start the service."""
    # Start the FastAPI app with Uvicorn in a subprocess
    with tempfile.TemporaryDirectory(delete=False) as output_dir:
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
        print("Starting FastAPI app with Uvicorn from dir {service_dir}...")
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

    return proc, output_dir


@pytest.mark.parametrize("config", [TEST_MYSQL_CONFIG])
def test_root_endpoints(service: Tuple, config: str):
    """Simple test to validate the example config and check the health endpoint."""
    # Unpack the service tuple and load the config
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

    # Handle any exceptions
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

    finally:
        # Terminate the Uvicorn server and cleanup
        print("Terminating the Uvicorn server...")
        proc.kill()
        proc.wait()
        # Force delete the output directory and all of its contents
        print(f"Deleting output directory: {output_dir}")
        subprocess.run(["rm", "-rf", output_dir])
