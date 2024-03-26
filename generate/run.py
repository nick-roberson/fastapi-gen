import os
from typing import Dict

from rich import print

from generate.backend.generate import (generate_files, install_backend_deps,
                                       lint_backend)
from generate.backend.openapi.export_openapi import export_openapi
from generate.backend.parse import load_config, parse_config, validate_config
from generate.frontend.generate import clear_output as clear_frontend_output
from generate.frontend.generate import (create_application,
                                        create_application_client,
                                        generate_app_main_page,
                                        install_dependencies, lint_frontend)
from generate.models import Config
from generate.utils import run_command


def load_and_validate_config(input_file: str) -> Dict:
    """Load the input yaml config file.

    Args:
        input_file (str): Path to the input yaml config.

    Returns:
        Dict: Dictionary of the loaded yaml config
    """
    loaded_config: Dict = load_config(input_file=input_file)
    validate_config(loaded_config)
    return parse_config(loaded_config)


def generate_back(config: Config, output_dir: str) -> Dict:
    """Generate the models and services from the input yaml config.

    Args:
        config (Config): Config object
        output_dir (str): Output directory
    Returns:
        Dict: Dictionary of the generated files
    """
    # (1) Generate the files
    print(f"Generating models and services ...")
    created_files = generate_files(output_dir=output_dir, config=config)
    print("Done!\n")

    # (2) Install the dependencies
    print(f"Installing dependencies using poetry ...")
    install_backend_deps(output_dir=output_dir)
    print("Done!\n")

    # (3) Export the OpenAPI JSON
    print(f"Exporting OpenAPI JSON ...")
    export_openapi(output_dir=output_dir)
    print("Done!\n")

    # (4) Lint the code
    print(f"Linting the code ...")
    lint_backend(output_dir=output_dir)
    print("Done!\n")

    return created_files


def generate_front(config: Config, output_dir: str, service_name: str) -> None:
    """Generates a typescript / react front end from scratch."""
    # (0) Clear the output directory
    print("Clearing the output directory ...")
    clear_frontend_output(output_dir=output_dir, service_name=service_name)
    print("Done!\n")

    # (1) Create the application
    print("Generating the frontend application...")
    create_application(output_dir=output_dir, service_name=service_name)
    print("Done!\n")

    # (2) Install the dependencies
    print("Installing node dependencies...")
    install_dependencies(output_dir=output_dir, service_name=service_name)
    print("Done!\n")

    # (3) Create the application client
    print("Generating the frontend service client code...")
    create_application_client(output_dir=output_dir, service_name=service_name)
    print("Done!\n")

    # (4) Generate the main page
    print("Generating the main page...")
    generate_app_main_page(
        output_dir=output_dir, service_name=service_name, models=config.models
    )
    print("Done!\n")

    # (5) Lint the code
    print("Linting the code...")
    lint_frontend(output_dir=output_dir, service_name=service_name)
    print("Done!\n")


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
        return generate_back(config=config, output_dir=output_dir)
    # Only regenerate the frontend
    if frontend_only:
        generate_front(config=config, output_dir=output_dir, service_name=service_name)
        return {}
    # Regenerate both the backend and frontend
    else:
        created_files = generate_back(config=config, output_dir=output_dir)
        generate_front(config=config, output_dir=output_dir, service_name=service_name)
        return created_files
