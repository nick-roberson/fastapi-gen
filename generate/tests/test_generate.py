import tempfile

import pytest

from generate.constants import SAMPLE_INPUT
from generate.generate import (generate_database, generate_managers,
                               generate_models, generate_services)
from generate.utils import load_config, parse_model_definition, validate_config


@pytest.mark.parametrize("config", [SAMPLE_INPUT])
def test_generate(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        # Parse the model definition
        config_def = load_config(config)
        db_config, model_config = parse_model_definition(config_def)

        # Generate the models
        generate_models(
            output_dir=output_dir,
            models=model_config.models,
        )

        # Generate the services
        generate_services(
            output_dir=output_dir,
            models=model_config.models,
        )

        # Generate the managers
        generate_managers(
            output_dir=output_dir,
            db_config=db_config,
            models=model_config.models,
        )

        # Generate the mongo
        generate_database(
            output_dir=output_dir,
            db_config=db_config,
        )
