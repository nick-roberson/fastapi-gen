import tempfile

import pytest

from generate.constants import SAMPLE_INPUT
from generate.generate import (generate_database, generate_managers,
                               generate_models, generate_services)
from generate.utils import load_config, parse_model_definition, validate_config


def test_validate():
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        # Load the config
        config = load_config(SAMPLE_INPUT)

        # Validate the config
        validate_config(config)

        # Parse the model definition
        db_config, model_config = parse_model_definition(config)

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
