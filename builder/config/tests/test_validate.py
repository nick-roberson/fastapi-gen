import tempfile

import pytest

from builder.config.parse import load_and_validate_config
from builder.constants import TEST_MYSQL_CONFIG


@pytest.mark.parametrize("config", [TEST_MYSQL_CONFIG])
def test_load_and_validate(config):
    """Simple test to load and validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        load_and_validate_config(config)
