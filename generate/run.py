import os
from typing import Dict

from rich import print

from generate.backend.generate import generate_files, lint_code
from generate.backend.openapi.export_openapi import export_openapi
from generate.backend.parse import load_config, parse_config, validate_config
from generate.frontend.generate import (create_application,
                                        create_application_client,
                                        install_dependencies)
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
    os.chdir(full_path)
    run_command("poetry install")
    run_command("poetry update")
    print("Installed dependencies!")

    # (4) Export the OpenAPI JSON
    print(f"\nExporting OpenAPI JSON ...")
    export_openapi(
        application_name="service:app",
        application_dir=output_dir,
        output_file=f"{output_dir}/openapi.json",
    )
    print("Exported OpenAPI JSON!")

    # (5) Lint the code
    print(f"\nLinting the code ...")
    lint_code(output_dir)
    print("Linted the code!")

    return result


def generate_front(output_dir: str, service_name: str) -> None:
    """Generates a typescript / react front end from scratch."""
    # (1) Create the application
    create_application(output_dir=output_dir, service_name=service_name)
    # (2) Install the dependencies
    install_dependencies(output_dir=output_dir, service_name=service_name)
    # (3) Create the application client
    create_application_client(output_dir=output_dir, service_name=service_name)


def generate(input_file: str, output_dir: str, service_name: str) -> Dict:
    """Generate the models and services from the input yaml config."""
    created_files = generate_back(output_dir=output_dir, input_file=input_file)
    generate_front(output_dir=output_dir, service_name=service_name)
    return created_files
