import os
from string import Template

from service_builder.constants import OPENAPI_SPEC_FN
from service_builder.jinja.templates import run_command

# Commands
TYPESCRIPT_CLIENT_CMD: Template = Template(
    "openapi-generator generate -i $openapi_spec -g typescript-fetch -o $output_dir"
)
PYTHON_CLIENT_CMD: Template = Template(
    "openapi-generator generate -i $openapi_spec -g python -o $output_dir"
)


def create_typescript_client(output_dir: str, service_name: str):
    """Generate the frontend service client code

    Args:
        output_dir (str): Output directory
        service_name (str): Name of the service
    """
    # Create the client code directory
    full_path = os.path.abspath(output_dir)
    client_code_dir = f"{full_path}/{service_name}/src/api"
    if not os.path.exists(client_code_dir):
        os.makedirs(client_code_dir, exist_ok=True)

    # Generate the client code
    command = TYPESCRIPT_CLIENT_CMD.substitute(
        openapi_spec=OPENAPI_SPEC_FN, output_dir=client_code_dir
    )
    run_command(cmd=command, cwd=full_path)


def create_python_client(output_dir: str):
    """Generate the python service client code

    Args:
        output_dir (str): Output directory
        service_name (str): Name of the service
    """
    # Create the client code directory
    full_path = os.path.abspath(output_dir)
    client_code_dir = f"{full_path}/client"
    if not os.path.exists(client_code_dir):
        os.makedirs(client_code_dir, exist_ok=True)

    # Generate the client code
    command = PYTHON_CLIENT_CMD.substitute(
        openapi_spec=OPENAPI_SPEC_FN, output_dir=client_code_dir
    )
    run_command(cmd=command, cwd=full_path)
