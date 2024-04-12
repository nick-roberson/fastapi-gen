import tempfile

import pytest

from builder.config.parse import load_config, parse_config, validate_config
from builder.constants import TEST_MONGO_CONFIG


@pytest.mark.parametrize("config", [TEST_MONGO_CONFIG])
def test_validate(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        config_def = load_config(config)
        validate_config(config_def)


@pytest.mark.parametrize("config", [TEST_MONGO_CONFIG])
def test_parse(config):
    """Simple test to parse the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        config_def = load_config(config)
        parse_config(config_def)
