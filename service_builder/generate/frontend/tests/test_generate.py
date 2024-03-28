import tempfile

import pytest

from service_builder.config.parse import load_config, parse_config
from service_builder.constants import SAMPLE_INPUT_FILE
from service_builder.generate.frontend.generate import (create_application,
                                                        generate_app_main_page,
                                                        install_dependencies,
                                                        lint_frontend)


@pytest.mark.parametrize("config", [SAMPLE_INPUT_FILE])
def test_generate(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        # Parse the model definitions
        config_def = load_config(config)
        config_model = parse_config(config_def)

        # Generate the application
        create_application(
            output_dir=output_dir, service_name=config_model.service_name
        )

        # Install the dependencies
        install_dependencies(
            output_dir=output_dir, service_name=config_model.service_name
        )

        # Generate the main page
        generate_app_main_page(
            output_dir=output_dir,
            service_name=config_model.service_name,
            models=config_model.models,
        )

        # Lint the code
        lint_frontend(output_dir=output_dir, service_name=config_model.service_name)
