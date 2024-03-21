import tempfile

import pytest

from generate.constants import SAMPLE_INPUT
from generate.generate import (generate_database, generate_managers,
                               generate_models, generate_services)
from generate.utils import load_config, parse_model_definition, validate_config


@pytest.mark.parametrize("config", [SAMPLE_INPUT])
def test_validate(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        # Parse the model definition
        config_def = load_config(config)
        # Validate
        validate_config(config_def)
