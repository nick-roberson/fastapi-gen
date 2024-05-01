import json
import os
from typing import Dict

import typer
from rich import print

from builder.config.parse import load_and_validate_config
from builder.models.configs import ServiceConfig


def validate_service_name(service_name: str) -> str:
    """Validate the service name and return the cleaned version.

    Args:
        service_name (str): The service name

    Returns:
        str: The cleaned service name
    """
    # Check if it is too short or too long
    if len(service_name) < 3:
        print("Service name must be at least 3 characters")
        typer.Exit(code=1)
    if len(service_name) > 20:
        print("Service name must be less than 20 characters")
        typer.Exit(code=1)

    # Clean the service name
    service_name = service_name.lower()
    service_name = "".join(e for e in service_name if e.isalnum())
    return service_name


def validate_config(config_file: str) -> ServiceConfig:
    """Validate the config file and return the absolute path.

    Args:
        config_file (str): The config file

    Returns:
        ServiceConfig: The validated config
    """
    # Check if the file exists
    if not os.path.exists(config_file):
        print(f"Config file not found at {config_file}")
        typer.Exit(code=1)

    # Get the absolute path
    full_path = os.path.abspath(config_file)

    # Load and validate the config
    config = load_and_validate_config(full_path)
    return config


def process_close(result: Dict, config: ServiceConfig, config_path: str):
    """Process the close out of the CLI command.

    Args:
        result (Dict): The generated files
        config (ServiceConfig): The service configuration
        config_path (str): The path to the config file
    """
    output_dir = config.output_dir

    # Display the generated files
    print(f"\nGenerated files:")
    print(json.dumps(result, indent=4))

    # Get rel path for the output dir
    rel_output_dir = os.path.relpath(output_dir)
    # Get rel path for the config file
    rel_config = os.path.relpath(config_path)

    # Display commands for users to go and run the generated files
    print("")
    print("Run Backend (Poetry):")
    print(
        f"\t% poetry run python main.py app run-backend --output-dir {rel_output_dir} --config {rel_config}"
    )
    print("")
    print("Run Frontend (NPM):")
    print(
        f"\t% poetry run python main.py app run-frontend --output-dir {rel_output_dir} --config {rel_config}"
    )
