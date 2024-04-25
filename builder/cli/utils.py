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


def validate_output_dir(output_dir: str):
    """Check if the output directory exists and create it if it doesn't.

    Args:
        output_dir (str): The output directory
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    return os.path.abspath(output_dir)


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


def process_close(result: Dict, output_dir: str, service_config: ServiceConfig):
    """Show the results and close the application.

    Args:
        result (Dict): The result of the generation
        output_dir (str): The output directory
        service_config (ServiceConfig): The service configuration
    """
    service_name = service_config.service_info.name

    # Display the generated files
    print(f"\nGenerated files:")
    print(json.dumps(result, indent=4))

    # Display commands for users to go and run the generated files
    print("")
    print("Run Backend (Poetry):")
    print(
        f"   % poetry run python main.py app run-backend --output-dir {output_dir} --config {output_dir}/{service_name}.yaml"
    )
    print("")
    print("Run Frontend (NPM):")
    print(
        f"   % poetry run python main.py app run-frontend --output-dir {output_dir} --config {output_dir}/{service_name}.yaml"
    )
