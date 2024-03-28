import tempfile

import pytest
from generate.backend.parse import load_config, parse_config
from generate.constants import SAMPLE_INPUT_FILE
from generate.frontend.generate import (create_application,
                                        generate_app_main_page,
                                        install_dependencies, lint_frontend)

# TODO: Uncomment the following imports when the generate_clients functionality is implemented
# from generate.clients.generate import create_typescript_client, create_python_clients


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

        # TODO: Generate the application client, currently commented out because of the missing OPENAPI_SPEC_FN
        # create_typescript_client(output_dir=output_dir, service_name=config_model.service_name)
        # create_python_clients(output_dir=output_dir, service_name=config_model.service_name)

        # Generate the main page
        generate_app_main_page(
            output_dir=output_dir,
            service_name=config_model.service_name,
            models=config_model.models,
        )

        # Lint the code
        lint_frontend(output_dir=output_dir, service_name=config_model.service_name)
