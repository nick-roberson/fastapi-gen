import os
import tempfile

import pytest

from builder.config.parse import load_config, parse_config
from builder.constants import TEST_MONGO_CONFIG, TEST_MYSQL_CONFIG
from builder.generate.docker.generator import DockerGenerator


@pytest.mark.parametrize("config", [TEST_MONGO_CONFIG, TEST_MYSQL_CONFIG])
def test_generate(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        # Parse the model definitions
        config_def = load_config(config)
        config = parse_config(config_def)

        # Init the backend generator
        generator = DockerGenerator(config=config, output_dir=output_dir)

        # Generate the backend code
        dockerfiles = generator.copy_dockerfiles()
        for dockerfile in dockerfiles:
            assert os.path.exists(dockerfile)

        # Clear the docker files
        generator.clear_docker_files()
        for dockerfile in dockerfiles:
            assert not os.path.exists(dockerfile)
