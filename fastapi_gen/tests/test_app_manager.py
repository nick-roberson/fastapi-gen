import copy
import os
import tempfile

import pytest

from fastapi_gen.app_manager import ApplicationManager
from fastapi_gen.config.parse import load_and_validate_config
from fastapi_gen.models.configs import ServiceConfig

# Path to the test restaurant configuration file
TEST_RESTAURANT_CONFIG_PATH: str = os.path.abspath(
    "fastapi_gen/tests/configs/restaurant.yaml"
)
# Load and validate the configuration
TEST_RESTAURANT_CONFIG: ServiceConfig = load_and_validate_config(
    TEST_RESTAURANT_CONFIG_PATH
)


@pytest.fixture
def app_manager():
    """Fixture to create an instance of ApplicationManager with a temporary output directory."""
    with tempfile.TemporaryDirectory() as output_dir:
        config = copy.deepcopy(TEST_RESTAURANT_CONFIG)
        config.output_dir = output_dir
        manager = ApplicationManager(config=config)
        yield manager


def test_app_manager_create(app_manager):
    """Test to create the application code and ensure cleanup post tests."""
    app_manager.generate()


def test_app_manager_full_stack(app_manager):
    """Test to generate full stack of the application."""
    app_manager.generate_full_stack()


def test_app_manager_backend_frontend(app_manager):
    """Test to generate separately backend and frontend of the application."""
    app_manager.generate_backend()
    app_manager.generate_frontend()


def test_app_manager_regenerate(app_manager):
    """Test to regenerate the application components."""
    app_manager.regenerate()
    app_manager.regenerate_frontend()
    app_manager.regenerate_backend()
