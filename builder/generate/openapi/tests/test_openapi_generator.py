import os
import tempfile

import pytest

from builder.config.parse import load_config, parse_config
from builder.constants import TEST_MYSQL_CONFIG
from builder.generate.openapi.generator import OpenAPIGenerator

TEST_OPENAPI_CONFIG_PATH: str = "builder/generate/openapi/tests/data/openapi.json"


@pytest.mark.parametrize("config", [TEST_MYSQL_CONFIG])
def test_openapi_generator(config):
    with tempfile.TemporaryDirectory() as output_dir:
        # Parse the model definitions
        config_def = load_config(config)
        config = parse_config(config_def)

        # Init the backend generator
        generator = OpenAPIGenerator(config=config)

        # Copy the openapi file to the backend code dir
        src = os.path.abspath(TEST_OPENAPI_CONFIG_PATH)
        dst = os.path.join(generator.backend_code_dir, "openapi.json")
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        os.system(f"cp {src} {dst}")

        # Generate the openapi code
        generator.generate_python_client()
        generator.generate_typescript_client()
