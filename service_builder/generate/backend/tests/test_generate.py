import tempfile

import pytest
from config.parse import load_config, parse_config
from constants import SAMPLE_INPUT_FILE
from generate.backend.generate import (
    generate_database,
    generate_managers,
    generate_models,
    generate_poetry_toml,
    generate_readme,
    generate_services,
    install_backend_deps,
    lint_backend,
)


@pytest.mark.parametrize("config", [SAMPLE_INPUT_FILE])
def test_generate(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        # Parse the model definitions
        config_def = load_config(config)
        config_model = parse_config(config_def)

        # Generate the models
        generate_models(
            output_dir=output_dir,
            config=config_model,
        )

        # Generate the services
        generate_services(
            output_dir=output_dir,
            config=config_model,
        )

        # Generate the managers
        generate_managers(
            output_dir=output_dir,
            config=config_model,
        )

        # Generate the mongo
        generate_database(
            output_dir=output_dir,
            config=config_model,
        )

        # Generate the poetry.toml
        generate_poetry_toml(
            output_dir=output_dir,
            config=config_model,
        )

        # Generate the README
        generate_readme(
            output_dir=output_dir,
        )

        # Install the dependencies
        install_backend_deps(
            output_dir=output_dir,
        )

        # TODO: Generate Open API Spec Json, currently commented out because the function cannot find the `fastapi` import for some reason
        # export_openapi(
        #     output_dir=output_dir,
        # )

        # Lint the code
        lint_backend(
            output_dir=output_dir,
        )
