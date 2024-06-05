import tempfile

import pytest

from fastapi_gen.config.parse import load_config, parse_config
from fastapi_gen.constants import TEST_MYSQL_CONFIG
from fastapi_gen.generate.docker.generator import DockerGenerator


@pytest.mark.parametrize("config", [TEST_MYSQL_CONFIG])
def test_docker_generator(config):
    """Simple test to validate the example config"""
    with tempfile.TemporaryDirectory() as output_dir:
        # Parse the model definitions
        config_def = load_config(config)
        config = parse_config(config_def)
        config.output_dir = output_dir

        # Create the frontend generator
        docker_generator = DockerGenerator(config=config)

        # Generate the docker files
        docker_generator.copy_dockerfiles()
        docker_generator.clear_docker_files()
