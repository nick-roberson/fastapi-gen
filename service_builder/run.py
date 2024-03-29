import logging
from typing import Dict

from service_builder.config.parse import (load_config, parse_config,
                                          validate_config)
from service_builder.generate.backend.generate import (copy_dockerfiles,
                                                       generate_files,
                                                       install_backend_deps,
                                                       lint_backend)
from service_builder.generate.clients.generate import (
    create_python_client, create_typescript_client)
from service_builder.generate.frontend.generate import (create_application,
                                                        generate_app_main_page,
                                                        install_dependencies,
                                                        lint_frontend)
from service_builder.models import ServiceConfig
from service_builder.openapi.export import export_openapi
from service_builder.utils import clear_directory


def load_and_validate_config(input_file: str) -> ServiceConfig:
    """Load the input yaml config file.

    Args:
        input_file (str): Path to the input yaml config.

    Returns:
        Dict: Dictionary of the loaded yaml config
    """
    loaded_config: Dict = load_config(input_file=input_file)
    validate_config(loaded_config)
    return parse_config(loaded_config)


def clear_backend_output(output_dir: str):
    """Clear the backend code directory

    Args:
        output_dir (str): Output directory
    """
    backend_code_dir = f"{output_dir}/src"
    clear_directory(backend_code_dir)


def clear_frontend_output(output_dir: str, service_name: str):
    """Clear the frontend code directory

    Args:
        output_dir (str): Output directory
        service_name (str): Name of the service
    """
    frontend_code_dir = f"{output_dir}/{service_name}"
    clear_directory(frontend_code_dir)


def clear_python_client(output_dir: str):
    """Clear the python client code directory

    Args:
        output_dir (str): Output directory
    """
    client_code_dir = f"{output_dir}/client"
    clear_directory(client_code_dir)


def clear_typescript_client(output_dir: str, service_name: str):
    """Clear the client code directory

    Args:
        output_dir (str): Output directory
        service_name (str): Name of the service
    """
    client_code_dir = f"{output_dir}/{service_name}/src/api"
    clear_directory(client_code_dir)


def generate_back(config: ServiceConfig, output_dir: str) -> Dict:
    """Generate the models and services from the input yaml config.

    Args:
        config (Config): Config object
        output_dir (str): Output directory
    Returns:
        Dict: Dictionary of the generated files
    """
    logging.info("Starting generating the backend code...\n")

    # (1) Clear the output directory
    logging.info("\tBACKEND: Clearing the backend code directory.")
    clear_backend_output(output_dir=output_dir)

    # (2) Generate the files
    logging.info("\tBACKEND: Generating models and services.")
    created_files = generate_files(output_dir=output_dir, config=config)

    # (3) Install the dependencies
    logging.info("\tBACKEND: Installing dependencies...")
    install_backend_deps(output_dir=output_dir)

    # (4) Copy Dockerfiles
    logging.info("\tBACKEND: Copying Dockerfiles...")
    docker_files = copy_dockerfiles(output_dir=output_dir)
    created_files["docker"] = docker_files

    # (5) Export the OpenAPI JSON
    logging.info("\tBACKEND: Exporting OpenAPI JSON...")
    openapi_file = export_openapi(output_dir=output_dir)
    created_files["openapi"] = [openapi_file]

    return created_files


def generate_front(config: ServiceConfig, output_dir: str, service_name: str) -> None:
    """Generates a typescript / react front end from scratch."""
    logging.info("Starting generating the frontend code...\n")

    # (0) Clear the output directory
    logging.info("\tFRONTEND: Clearing the frontend code directory.")
    clear_frontend_output(output_dir=output_dir, service_name=service_name)

    # (1) Create the application
    logging.info("\tFRONTEND: Creating the application.")
    create_application(output_dir=output_dir, service_name=service_name)

    # (2) Install the dependencies
    logging.info("\tFRONTEND: Installing dependencies.")
    install_dependencies(output_dir=output_dir, service_name=service_name)

    # (3) Generate the main page
    logging.info("\tFRONTEND: Generating the main page.")
    generate_app_main_page(
        output_dir=output_dir, service_name=service_name, models=config.models
    )


def generate_clients(output_dir: str, service_name: str):
    """Generate the frontend service client code

    Args:
        output_dir (str): Output directory
        service_name (str): Name of the service
        models (List[ModelConfig]): List of model configurations
    """
    logging.info("Starting generating the client code...\n")

    logging.info("\tCLIENTS: Completed clearing the typescript / python client dirs.")
    clear_typescript_client(output_dir=output_dir, service_name=service_name)
    clear_typescript_client(output_dir=output_dir, service_name=service_name)

    logging.info("\tCLIENTS: Generating the typescript / python client code.")
    create_typescript_client(output_dir=output_dir, service_name=service_name)

    logging.info("\tCLIENTS: Generating the python client code.")
    create_python_client(output_dir=output_dir)


def lint_generated_code(output_dir: str, service_name: str):
    """Lint the generated code.

    Args:
        output_dir (str): Output directory
        service_name (str): Name of the service
    """
    logging.info("Starting linting the generated code...\n")

    logging.info("\tLINT: Linting frontend code.")
    lint_frontend(output_dir=output_dir, service_name=service_name)

    logging.info("\tLINT: Linting backend code.")
    lint_backend(output_dir=output_dir)


def generate(
    input_file: str,
    output_dir: str,
    service_name: str,
    backend_only: bool = False,
    frontend_only: bool = False,
) -> Dict:
    """Generate the models and services from the input yaml config.

    Args:
        input_file (str): Path to the input yaml config.
        output_dir (str): Output directory
        service_name (str): Name of the service.
        backend_only (bool): Only regenerate the backend
        frontend_only (bool): Only regenerate the frontend
    Returns:
        Dict: Dictionary of the generated files
    """
    config = load_and_validate_config(input_file)

    # Only regenerate the backend
    if backend_only:
        created_files = generate_back(config=config, output_dir=output_dir)
        generate_clients(output_dir=output_dir, service_name=service_name)
        lint_backend(output_dir=output_dir)
        return created_files

    # Only regenerate the frontend
    if frontend_only:
        generate_front(config=config, output_dir=output_dir, service_name=service_name)
        lint_frontend(output_dir=output_dir, service_name=service_name)
        return {}

    # Regenerate both the backend and frontend
    else:
        created_files = generate_back(config=config, output_dir=output_dir)
        generate_front(config=config, output_dir=output_dir, service_name=service_name)
        generate_clients(output_dir=output_dir, service_name=service_name)
        lint_generated_code(output_dir=output_dir, service_name=service_name)
        return created_files
