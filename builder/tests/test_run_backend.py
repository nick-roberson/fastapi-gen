import os
import subprocess
import tempfile
import time
from typing import Tuple

import httpx
import pytest

from builder.config.parse import load_config, parse_config
from builder.constants import TEST_MYSQL_CONFIG
from builder.generate.backend.generator import BackendGenerator


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
        host = "127.0.0.1"
        port = 8000
        proc = subprocess.Popen(
            ["uvicorn", "service:app", "--host", host, "--port", str(port), "--reload"],
            cwd=service_dir,
        )

    return host, port, proc, output_dir


@pytest.mark.parametrize("config", [TEST_MYSQL_CONFIG])
def test_root_endpoints(service: Tuple, config: str):
    """Simple test to validate the example config and check the health endpoint."""
    # Unpack the service tuple and load the config
    host, port, proc, output_dir = service

    # Check the health endpoint
    print(f"Running Uvicorn on http://{host}:{port} and hitting the health endpoint...")
    try:
        # Give Uvicorn a moment to start
        time.sleep(3)  # Adjust sleep time if necessary

        # Perform HTTP GET request to the health endpoint
        response = httpx.get(f"http://{host}:{port}/health")
        assert response.status_code == 200
        assert response.json() == {"message": "Healthy"}

        # Perform HTTP GET request to the ready endpoint
        response = httpx.get(f"http://{host}:{port}/ready")
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
        # Delete the output directory
        print(f"Cleaning up output directory {output_dir}")
        os.rmdir(output_dir)
