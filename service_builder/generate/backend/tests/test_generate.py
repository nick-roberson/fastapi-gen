import tempfile

import pytest

from service_builder.config.parse import load_config, parse_config
from service_builder.constants import SAMPLE_INPUT_FILE
from service_builder.generate.backend.generator import BackendGenerator


@pytest.mark.parametrize("config", [SAMPLE_INPUT_FILE])
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
        generator.generate_managers()
        generator.generate_database()
        generator.generate_poetry_toml()
        generator.generate_readme()
        generator.install_backend_deps()
        generator.lint_backend()
