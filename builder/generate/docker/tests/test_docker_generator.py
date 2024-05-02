import tempfile

import pytest

from builder.config.parse import load_config, parse_config
from builder.constants import TEST_MYSQL_CONFIG
from builder.generate.docker.generator import DockerGenerator


@pytest.mark.parametrize("config", [TEST_MYSQL_CONFIG])
def test_docker_generator(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        # Parse the model definitions
        config_def = load_config(config)
        config = parse_config(config_def)

        # Create the frontend generator
        docker_generator = DockerGenerator(config=config)

        # Generate the docker files
        docker_generator.copy_dockerfiles()
        docker_generator.clear_docker_files()
