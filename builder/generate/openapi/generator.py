import os
from string import Template
from typing import List

from rich import print

from builder.constants import OPENAPI_SPEC_FN
from builder.models import ServiceConfig
from builder.openapi.export import export_openapi
from builder.utils import run_command

# Command templates for generating client code using the OpenAPI Generator
PYTHON_CLIENT_CMD: Template = Template(
    "openapi-generator generate -i $openapi_spec -g python -o $output_dir"
)
TYPESCRIPT_CLIENT_CMD: Template = Template(
    "openapi-generator generate -i $openapi_spec -g typescript-fetch -o $output_dir"
)


class OpenAPIGenerator:
    """
    A class responsible for managing OpenAPI specification files and generating client libraries.

    Attributes:
        config (ServiceConfig): Configuration data for the service.
        output_dir (str): Base directory for output files.
        backend_code_dir (str): Directory for backend code.
        openapi_file_path (str): Full path to the OpenAPI JSON file.
        python_client_dir (str): Directory for the Python client library.
        typescript_client_dir (str): Directory for the TypeScript client library.
    """

    def __init__(self, config: ServiceConfig):
        """
        Initialize the OpenAPIGenerator with a service configuration.

        Parameters:
            config (ServiceConfig): Configuration object for the service.
        """
        self.config = config
        self.output_dir = config.output_dir
        self.backend_code_dir = os.path.join(self.output_dir, "backend")
        self.openapi_file_path = os.path.join(self.backend_code_dir, OPENAPI_SPEC_FN)
        os.makedirs(self.backend_code_dir, exist_ok=True)

        self.python_client_dir = os.path.join(self.output_dir, "client")
        self.typescript_client_dir = os.path.join(
            self.output_dir, config.service_info.name, "src/api"
        )

    def generate_openapi_json(self) -> str:
        """
        Generate and return the path to the OpenAPI JSON specification file.

        Returns:
            str: The path to the generated OpenAPI JSON file.
        """
        output_file = export_openapi(output_dir=self.backend_code_dir)
        print(f"\t\t> OpenAPI spec generated at: {output_file}")
        return output_file

    def validate_openapi_spec(self):
        """
        Optional method to validate the generated OpenAPI specification.

        Implement validation logic or integrate with an external validation tool if necessary.
        """
        pass

    def generate_python_client(self):
        """
        Generate the Python client library using the OpenAPI Generator.
        """
        if not os.path.exists(self.python_client_dir):
            os.makedirs(self.python_client_dir, exist_ok=True)
        command = PYTHON_CLIENT_CMD.substitute(
            openapi_spec=self.openapi_file_path, output_dir=self.python_client_dir
        )
        run_command(cmd=command, cwd=self.backend_code_dir)

    def generate_typescript_client(self):
        """
        Generate the TypeScript client library using the OpenAPI Generator.
        """
        if not os.path.exists(self.typescript_client_dir):
            os.makedirs(self.typescript_client_dir, exist_ok=True)
        command = TYPESCRIPT_CLIENT_CMD.substitute(
            openapi_spec=self.openapi_file_path, output_dir=self.typescript_client_dir
        )
        run_command(cmd=command, cwd=self.backend_code_dir)
