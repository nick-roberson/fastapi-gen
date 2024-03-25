import os
from string import Template

from generate.utils import run_command

OPENAPI_SPEC_FN: str = "openapi.json"

# Commands
CREATE_SERVICE_CMD: Template = Template(
    "npx create-react-app $service_name --template typescript"
)
CREATE_MODEL_CMD: Template = Template(
    "openapi-generator generate -i $openapi_spec -g python -o $output_dir"
)

# Node Dependencies
NODE_DEPENDENCIES = [
    "axios",
    "@mui/material",
    "@mui/icons-material",
    "@mui/lab",
]


def cd_to_output_dir(output_dir: str):
    """Change to the output directory."""
    full_path = os.path.abspath(output_dir)
    if not os.path.exists(full_path):
        os.makedirs(full_path, exist_ok=True)
    os.chdir(full_path)


def create_application(output_dir: str, service_name: str):
    """Generates a typescript / react front end from scratch.

    TODO:
        - Import the openapi schema
        - Generate the typescript models
        - Generate the react components
    """
    # (1) navigate to the output directory
    full_path = os.path.abspath(output_dir)
    cd_to_output_dir(full_path)

    # (2) Generate the application
    print("Generating the frontend application...")
    command = CREATE_SERVICE_CMD.substitute(service_name=service_name)
    run_command(command)
    print("Done!")


def install_dependencies(output_dir: str):
    """Install node dependencies using npm"""
    # (1) navigate to the output directory
    full_path = os.path.abspath(output_dir)
    cd_to_output_dir(full_path)

    # (2) Install the dependencies
    for dep in NODE_DEPENDENCIES:
        run_command(f"npm install {dep}")


def create_application_client(output_dir: str, service_name: str):
    """Generate the frontend service client code"""
    # (1) Generate the front end service code
    print("Generating the frontend service client code...")
    full_path = os.path.abspath(output_dir)
    client_code_dir = f"{full_path}/{service_name}/src/api"
    command = CREATE_MODEL_CMD.substitute(
        openapi_spec=OPENAPI_SPEC_FN, output_dir=client_code_dir
    )
    run_command(command)
    print("Done!")
