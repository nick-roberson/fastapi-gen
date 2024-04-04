import os
from string import Template
from typing import List

from jinja2 import Environment, FileSystemLoader

from service_builder.constants import (FRONTEND_TEMPLATES, NODE_DEPENDENCIES,
                                       OPENAPI_SPEC_FN)
from service_builder.models import ModelConfig, ServiceConfig
from service_builder.utils import run_command

# Commands
CREATE_SERVICE_CMD: Template = Template(
    "npx create-react-app $service_name --template typescript"
)
CREATE_MODEL_CMD: Template = Template(
    "openapi-generator generate -i $openapi_spec -g typescript-fetch -o $output_dir"
)
INSTALL_DEPENDENCIES_CMD: Template = Template("npm install $dependencies")


def create_application(config: ServiceConfig, output_dir: str):
    """Generates a typescript / react front end from scratch.

    Args:
        config (ServiceConfig): Service configuration
        output_dir (str): Output directory
    """
    service_name = config.service_info.name
    full_path = os.path.abspath(output_dir)
    command = CREATE_SERVICE_CMD.substitute(service_name=service_name)
    run_command(cmd=command, cwd=full_path)


def install_dependencies(config: ServiceConfig, output_dir: str):
    """Install node dependencies using npm

    Args:
        config (ServiceConfig): Service configuration
        output_dir (str): Output directory
    """
    service_name = config.service_info.name
    full_path = os.path.abspath(output_dir)
    app_path = f"{full_path}/{service_name}"
    dependencies = " ".join(NODE_DEPENDENCIES)
    command = INSTALL_DEPENDENCIES_CMD.substitute(dependencies=dependencies)
    run_command(cmd=command, cwd=app_path)


def create_typescript_client(output_dir: str, service_name: str):
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


def lint_frontend(config: ServiceConfig, output_dir: str):
    """Lint the code using prettier

    Args:
        config (ServiceConfig): Service configuration
        output_dir (str): Output directory
    """
    service_name = config.service_info.name
    code_path = f"{output_dir}/{service_name}/src"
    run_command("npx prettier --write .", cwd=code_path)
    run_command("npx eslint --fix .", cwd=code_path)


def generate_app_main_page(config: ServiceConfig, output_dir: str):
    """Generate the main page of the application

    Args:
        config (ServiceConfig): Service configuration
        output_dir (str): Output directory
    """
    # Load the template
    env = Environment(loader=FileSystemLoader(FRONTEND_TEMPLATES))
    frontend_template = env.get_template("App.tsx")

    # Generate the models
    output = frontend_template.render(models=config.models)

    # Write the models to the output directory
    service_name = config.service_info.name
    file_name = f"{output_dir}/{service_name}/src/App.tsx"
    if not os.path.exists(file_name):
        os.makedirs(os.path.dirname(file_name), exist_ok=True)

    # Write the models to the output directory
    with open(file_name, "w") as f:
        f.write(output)

    return file_name
