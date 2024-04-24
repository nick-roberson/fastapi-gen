import os
import tempfile

import pytest

from builder.config.parse import load_config, parse_config
from builder.constants import TEST_MONGO_CONFIG
from builder.generate.poetry.generator import PoetryGenerator


@pytest.mark.parametrize("config", [TEST_MONGO_CONFIG])
def test_generate(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        # Parse the model definitions
        config_def = load_config(config)
        config = parse_config(config_def)

        # Init the backend generator
        generator = PoetryGenerator(config=config, output_dir=output_dir)

        # Generate the backend code
        generator.generate_poetry_toml()
        assert os.path.exists(generator.poetry_toml)

        # Install the dependencies
        generator.install_dependencies()
        assert os.path.exists(generator.poetry_lock)

        # Export requirements
        generator.export_requirements()
        assert os.path.exists(generator.requirements_txt)
