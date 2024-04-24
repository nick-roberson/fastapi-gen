import os
from string import Template
from typing import Dict, List

from rich import print

from builder.constants import OPENAPI_SPEC_FN
from builder.models import ServiceConfig
from builder.openapi.export import export_openapi
from builder.utils import run_command

# Generate python client command
PYTHON_CLIENT_CMD: Template = Template(
    "openapi-generator generate -i $openapi_spec -g python -o $output_dir"
)
# Create Typescript Client command
TYPESCRIPT_CLIENT_CMD: Template = Template(
    "openapi-generator generate -i $openapi_spec -g typescript-fetch -o $output_dir"
)


class OpenAPIGenerator:
    """Class to handle the generation and management of OpenAPI specifications."""

    def __init__(self, config: ServiceConfig, output_dir: str):
        # Set the config and output directory
        self.config = config
        self.output_dir = output_dir

        # Set the code directory
        self.backend_code_dir = os.path.join(output_dir, "backend")
        self.openapi_file_path = os.path.join(self.backend_code_dir, OPENAPI_SPEC_FN)
        if not os.path.exists(self.backend_code_dir):
            os.makedirs(self.backend_code_dir, exist_ok=True)

        # Set the client code directories
        self.python_client_dir = os.path.join(self.output_dir, "client")
        self.typescript_client_dir = os.path.join(
            output_dir, config.service_info.name, "src/api"
        )

    def generate_openapi_json(self) -> str:
        """Generate the OpenAPI JSON file."""
        output_file = export_openapi(output_dir=self.backend_code_dir)
        print(f"\t\t> OpenAPI spec generated at: {output_file}")
        return output_file

    def validate_openapi_spec(self):
        """Optional method to validate the OpenAPI specification."""
        # Implement validation logic or integrate with an external tool
        pass

    def generate_python_client(self):
        """Generate the python client code"""
        # Create the client code directory
        if not os.path.exists(self.python_client_dir):
            os.makedirs(self.python_client_dir, exist_ok=True)

        # Generate the client code
        command = PYTHON_CLIENT_CMD.substitute(
            openapi_spec=OPENAPI_SPEC_FN, output_dir=self.python_client_dir
        )
        run_command(cmd=command, cwd=self.backend_code_dir)

    def generate_typescript_client(self):
        """Generate the typescript client code"""
        # Create the client code directory
        if not os.path.exists(self.typescript_client_dir):
            os.makedirs(self.typescript_client_dir, exist_ok=True)

        # Generate the client code
        command = TYPESCRIPT_CLIENT_CMD.substitute(
            openapi_spec=OPENAPI_SPEC_FN, output_dir=self.typescript_client_dir
        )
        run_command(cmd=command, cwd=self.backend_code_dir)
