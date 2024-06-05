import tempfile

import pytest

from fastapi_gen.config.parse import load_config, parse_config
from fastapi_gen.constants import TEST_MYSQL_CONFIG


@pytest.mark.parametrize("config", [TEST_MYSQL_CONFIG])
def test_config_not_exists(config):
    with pytest.raises(ValueError):
        load_config("not_exists.yaml")


@pytest.mark.parametrize("config", [TEST_MYSQL_CONFIG])
def test_config_missing_service(config):
    with pytest.raises(ValueError):
        config_def = load_config(config)
        del config_def["service"]
        parse_config(config_def)


@pytest.mark.parametrize("config", [TEST_MYSQL_CONFIG])
def test_config_missing_models(config):
    with pytest.raises(ValueError):
        config_def = load_config(config)
        del config_def["models"]
        parse_config(config_def)


@pytest.mark.parametrize("config", [TEST_MYSQL_CONFIG])
def test_config_missing_database(config):
    with pytest.raises(ValueError):
        config_def = load_config(config)
        del config_def["database"]
        parse_config(config_def)


@pytest.mark.parametrize("config", [TEST_MYSQL_CONFIG])
def test_config_missing_model_missing_fields(config):
    with pytest.raises(ValueError):
        config_def = load_config(config)
        del config_def["models"][0]["fields"]
        parse_config(config_def)
