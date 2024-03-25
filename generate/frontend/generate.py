import os
from string import Template

from rich import print

from generate.utils import run_command

OPENAPI_SPEC_FN: str = "openapi.json"

# Commands
CREATE_SERVICE_CMD: Template = Template(
    "npx create-react-app $service_name --template typescript"
)
CREATE_MODEL_CMD: Template = Template(
    "openapi-generator generate -i $openapi_spec -g python -o $output_dir"
)
INSTALL_DEPENDENCIES_CMD: Template = Template("npm install $dependency")

# Node Dependencies
NODE_DEPENDENCIES = [
    "axios",
    "@mui/material",
    "@mui/icons-material",
    "@mui/lab",
]


def create_application(output_dir: str, service_name: str):
    """Generates a typescript / react front end from scratch.

    Args:
        output_dir (str): Output directory
        service_name (str): Name of the service
    """
    full_path = os.path.abspath(output_dir)
    command = CREATE_SERVICE_CMD.substitute(service_name=service_name)
    run_command(cmd=command, cwd=full_path)


def install_dependencies(output_dir: str, service_name: str):
    """Install node dependencies using npm

    Args:
        output_dir (str): Output directory
        service_name (str): Name of the service
    """
    full_path = os.path.abspath(output_dir)
    app_path = f"{full_path}/{service_name}"
    for dependency in NODE_DEPENDENCIES:
        command = INSTALL_DEPENDENCIES_CMD.substitute(dependency=dependency)
        run_command(cmd=command, cwd=app_path)


def create_application_client(output_dir: str, service_name: str):
    """Generate the frontend service client code

    Args:
        output_dir (str): Output directory
        service_name (str): Name of the service
    """
    full_path = os.path.abspath(output_dir)
    client_code_dir = f"{full_path}/{service_name}/src/api"

    command = CREATE_MODEL_CMD.substitute(
        openapi_spec=OPENAPI_SPEC_FN, output_dir=client_code_dir
    )
    run_command(cmd=command, cwd=full_path)
