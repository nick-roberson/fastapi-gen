import tempfile

import pytest

from builder.config.parse import load_config, parse_config
from builder.constants import TEST_MONGO_CONFIG, TEST_MYSQL_CONFIG
from builder.generate.backend.generator import BackendGenerator
from builder.generate.linting.manager import LintingManager


@pytest.mark.parametrize("config", [TEST_MONGO_CONFIG, TEST_MYSQL_CONFIG])
def test_generate(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        # Parse the model definitions
        config_def = load_config(config)
        config = parse_config(config_def)

        # Init the backend generator
        generator = BackendGenerator(config=config, output_dir=output_dir)

        # Generate the backend code
        generator.generate_models()
        generator.generate_services()
        generator.generate_templated_components()
        generator.generate_database()
        generator.generate_readme()

        # Lint the frontend
        linting_manager = LintingManager(config=config, output_dir=output_dir)
        linting_manager.lint_backend()
