import os
import tempfile

import pytest

from fastapi_gen.config.parse import load_config, parse_config
from fastapi_gen.constants import TEST_MYSQL_CONFIG
from fastapi_gen.generate.poetry.generator import PoetryGenerator


@pytest.mark.parametrize("config", [TEST_MYSQL_CONFIG])
def test_generate(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        # Parse the model definitions
        config_def = load_config(config)
        config = parse_config(config_def)

        # Init the backend generator
        generator = PoetryGenerator(config=config)

        # Generate the backend code
        generator.generate_poetry_toml()
        assert os.path.exists(generator.poetry_toml)

        # Install the dependencies
        generator.install_dependencies()
        assert os.path.exists(generator.poetry_lock)

        # Export requirements
        generator.export_requirements()
        assert os.path.exists(generator.requirements_txt)
