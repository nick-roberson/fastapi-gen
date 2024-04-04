import tempfile

import pytest

from service_builder.config.parse import load_config, parse_config
from service_builder.constants import SAMPLE_INPUT_FILE
from service_builder.generate.backend.generate import (generate_database,
                                                       generate_managers,
                                                       generate_models,
                                                       generate_poetry_toml,
                                                       generate_readme,
                                                       generate_services,
                                                       install_backend_deps,
                                                       lint_backend)


@pytest.mark.parametrize("config", [SAMPLE_INPUT_FILE])
def test_generate(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        # Parse the model definitions
        config_def = load_config(config)
        config = parse_config(config_def)

        # Generate the models
        generate_models(config=config, output_dir=output_dir)
        # Generate the services
        generate_services(config=config, output_dir=output_dir)
        # Generate the managers
        generate_managers(config=config, output_dir=output_dir)
        # Generate the mongo
        generate_database(config=config, output_dir=output_dir)
        # Generate the poetry.toml
        generate_poetry_toml(config=config, output_dir=output_dir)

        # Generate the README
        generate_readme(output_dir=output_dir)
        # Install the dependencies
        install_backend_deps(output_dir=output_dir)
        # Lint the code
        lint_backend(output_dir=output_dir)
