import tempfile

import pytest

from builder.config.parse import load_config, parse_config
from builder.constants import SAMPLE_INPUT_FILE
from builder.generate.frontend.generator import FrontendGenerator


@pytest.mark.parametrize("config", [SAMPLE_INPUT_FILE])
def test_generate(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        # Parse the model definitions
        config_def = load_config(config)
        config = parse_config(config_def)

        # Create the frontend generator
        frontend_generator = FrontendGenerator(config=config, output_dir=output_dir)

        # Generate the application
        frontend_generator.generate_application()
        # Install the dependencies
        frontend_generator.install_dependencies()
        # Generate the main page
        frontend_generator.generate_templated_components()
        # Lint the code
        frontend_generator.lint_frontend()
