import tempfile

import pytest
from config.parse import load_config, parse_config, validate_config
from constants import SAMPLE_INPUT_FILE


@pytest.mark.parametrize("config", [SAMPLE_INPUT_FILE])
def test_validate(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        config_def = load_config(config)
        validate_config(config_def)


@pytest.mark.parametrize("config", [SAMPLE_INPUT_FILE])
def test_parse(config):
    """Simple test to parse the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        config_def = load_config(config)
        parse_config(config_def)
