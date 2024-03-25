import os
from typing import Dict

from rich import print

from generate.backend.generate import generate_files, lint_backend
from generate.backend.openapi.export_openapi import export_openapi
from generate.backend.parse import load_config, parse_config, validate_config
from generate.frontend.generate import (
    create_application,
    create_application_client,
    install_dependencies,
    lint_frontend,
)
from generate.models import Config
from generate.utils import run_command


def generate_back(output_dir: str, input_file: str) -> Dict:
    """Generate the models and services from the input yaml config.

    Args:
        output_dir (str): Output directory
        input_file (str): Path to the input yaml config.

    Returns:
        Dict: Dictionary of the generated files
    """
    # (1) Load and validate the config
    print(f"Loading and validating the config ...")
    loaded_config: Dict = load_config(input_file=input_file)
    validate_config(loaded_config)
    config: Config = parse_config(loaded_config)
    print("Loaded and validated the config!")

    # (2) Generate the files
    print(f"\nGenerating models and services ...")
    result = generate_files(output_dir, config, is_revert=False)
    print("Generated models and services!")

    # (3) Install the dependencies
    print(f"\nInstalling dependencies using poetry ...")
    full_path = os.path.abspath(output_dir)
    cmd = "poetry install"
    run_command(cmd=cmd, cwd=full_path)
    print("Installed dependencies!")

    # (4) Export the OpenAPI JSON
    print(f"\nExporting OpenAPI JSON ...")
    application_name = "service:app"
    openapi_json_file = f"{output_dir}/openapi.json"
    export_openapi(
        application_name=application_name,
        application_dir=output_dir,
        output_file=openapi_json_file,
    )
    print("Exported OpenAPI JSON!")

    # (5) Lint the code
    print(f"\nLinting the code ...")
    lint_backend(output_dir=output_dir)
    print("Linted the code!")

    return result


def generate_front(output_dir: str, service_name: str) -> None:
    """Generates a typescript / react front end from scratch."""
    # (1) Create the application
    print("Generating the frontend application...")
    create_application(output_dir=output_dir, service_name=service_name)
    print("Done!")

    # (2) Install the dependencies
    print("Installing node dependencies...")
    install_dependencies(output_dir=output_dir, service_name=service_name)
    print("Done!")

    # (3) Create the application client
    print("Generating the frontend service client code...")
    create_application_client(output_dir=output_dir, service_name=service_name)
    print("Done!")

    # (4) Lint the code
    print("Linting the code...")
    lint_frontend(output_dir=output_dir, service_name=service_name)
    print("Done!")


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
    # Only regenerate the backend
    if backend_only:
        return generate_back(output_dir=output_dir, input_file=input_file)
    # Only regenerate the frontend
    if frontend_only:
        generate_front(output_dir=output_dir, service_name=service_name)
        return {}
    # Regenerate both the backend and frontend
    else:
        created_files = generate_back(output_dir=output_dir, input_file=input_file)
        generate_front(output_dir=output_dir, service_name=service_name)
        return created_files
