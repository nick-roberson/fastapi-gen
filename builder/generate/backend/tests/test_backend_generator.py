import tempfile

import pytest

from builder.config.parse import load_config, parse_config
from builder.constants import TEST_MYSQL_CONFIG
from builder.generate.backend.generator import BackendGenerator


@pytest.mark.parametrize("config", [TEST_MYSQL_CONFIG])
def test_backend_generator(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        # Parse the model definitions
        config_def = load_config(config)
        config = parse_config(config_def)
        config.output_dir = output_dir

        # Init the backend generator
        generator = BackendGenerator(config=config)

        # Generate the backend code
        generator.generate_models()
        generator.generate_services()
        generator.generate_templated_components()
        generator.generate_database()
        generator.generate_readme()
