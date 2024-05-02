import copy
import os
import tempfile

import pytest

from builder.app_manager import ApplicationManager
from builder.config.parse import load_and_validate_config
from builder.models.configs import ServiceConfig

# Constants to store the config and parameters for the tests
TEST_RESTAURANT_CONFIG: str = os.path.abspath("builder/tests/configs/restaurant.yaml")

# Load and validate the restaurant config
TEST_RESTAURANT_CONFIG: ServiceConfig = load_and_validate_config(TEST_RESTAURANT_CONFIG)


# Fixture to create the code and start the service
@pytest.mark.parametrize("config", [TEST_RESTAURANT_CONFIG])
def test_app_manager_create(config):
    """Fixture to create the code and start the service, and ensure cleanup after tests."""
    # Create a temporary directory that will be cleaned up automatically
    with tempfile.TemporaryDirectory() as output_dir:
        print(f"Output directory: {output_dir}")
        config = copy.copy(TEST_RESTAURANT_CONFIG)
        config.output_dir = output_dir

        # (1) Init the application manager
        app_manager = ApplicationManager(config=config)
        app_manager.generate()


@pytest.mark.parametrize("config", [TEST_RESTAURANT_CONFIG])
def test_app_manager_create(config):
    """Fixture to create the code and start the service, and ensure cleanup after tests."""
    # Create a temporary directory that will be cleaned up automatically
    with tempfile.TemporaryDirectory() as output_dir:
        print(f"Output directory: {output_dir}")
        config = copy.copy(TEST_RESTAURANT_CONFIG)
        config.output_dir = output_dir

        # (1) Init the application manager
        app_manager = ApplicationManager(config=config)
        app_manager.generate_full_stack()


@pytest.mark.parametrize("config", [TEST_RESTAURANT_CONFIG])
def test_app_manager_create(config):
    """Fixture to create the code and start the service, and ensure cleanup after tests."""
    # Create a temporary directory that will be cleaned up automatically
    with tempfile.TemporaryDirectory() as output_dir:
        print(f"Output directory: {output_dir}")
        config = copy.copy(TEST_RESTAURANT_CONFIG)
        config.output_dir = output_dir

        # (1) Init the application manager
        app_manager = ApplicationManager(config=config)
        app_manager.generate_backend()
        app_manager.generate_frontend()


@pytest.mark.parametrize("config", [TEST_RESTAURANT_CONFIG])
def test_app_manager_regenerate(config):
    """Fixture to create the code and start the service, and ensure cleanup after tests."""
    # Create a temporary directory that will be cleaned up automatically
    with tempfile.TemporaryDirectory() as output_dir:
        print(f"Output directory: {output_dir}")
        config = copy.copy(TEST_RESTAURANT_CONFIG)
        config.output_dir = output_dir

        # (1) Init the application manager
        app_manager = ApplicationManager(config=config)
        app_manager.regenerate()
        app_manager.regenerate_frontend()
        app_manager.regenerate_backend()
