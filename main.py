import logging
import os
from typing import Dict, Optional

import typer
from rich import print

from service_builder.config.parse import load_and_validate_config
from service_builder.constants import (DEFAULT_PORT, SAMPLE_INPUT_FILE,
                                       SAMPLE_OUTPUT_DIR)
from service_builder.generate.backend.generator import BackendGenerator
from service_builder.generate.frontend.generate import FrontendGenerator
from service_builder.models.configs import ServiceConfig
from service_builder.run import generate as generate_service

app = typer.Typer()


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
    code_dir = "src"

    # Display the generated files
    print(f"\nGenerated files:")
    for key, value in result.items():

        # Handle logging files
        if key.endswith("Files"):
            print(f"\t{key}:")
            for file_type, file_names in value.items():
                print(f"\t\t{file_type}: {file_names}")

        # Handle logging directories
        elif key.endswith("Directories"):
            print(f"\t{key}:")
            for dir_type, dir_names in value.items():
                print(f"\t\t{dir_type}: {dir_names}")

    # Display commands for users to go and run the generated files
    print("\nRun the following commands to run the service:")
    print(f"\t% cd {output_dir}/{code_dir}")
    print(f"\t% poetry run uvicorn service:app --reload --port {DEFAULT_PORT}")

    # Display the frontend commands
    service_name = service_config.service_info.name
    print("\nRun the following commands to run the frontend:")
    print(f"\t% cd {output_dir}/{service_name}")
    print(f"\t% npm start")


@app.command()
def generate_typescript_app(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
    output_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--output-dir", "-o", help="Path to the output directory."
    ),
):
    """Generate a React frontend from the input yaml config.

    Args:
        config (Optional[str], optional): Path to the input yaml config.
            Defaults to SAMPLE_INPUT_FILE.
        output_dir (Optional[str], optional): Path to the output directory.
            Defaults to SAMPLE_OUTPUT_DIR.
    """
    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    output_directory = validate_output_dir(output_dir)
    context = {
        "service_config": service_config,
        "output_dir": output_directory,
        "frontend_only": True,
    }

    # Log the inputs
    service_name = service_config.service_info.name
    print(f"Generating Frontend service for app `{service_name}`")
    print(f"\tconfig:     {config}")
    print(f"\toutput_dir: {output_dir}\n")

    # Generate the frontend files and close out
    result = generate_service(**context)
    process_close(
        result=result, output_dir=output_directory, service_config=service_config
    )


@app.command()
def generate_python_app(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
    output_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--output-dir", "-o", help="Path to the output directory."
    ),
):
    """Generate a FastAPI backend from the input yaml config.

    Args:
        config (Optional[str], optional): Path to the input yaml config.
            Defaults to SAMPLE_INPUT_FILE.
        output_dir (Optional[str], optional): Path to the output directory.
            Defaults to SAMPLE_OUTPUT_DIR.
    """
    # Validate the input and get absolute paths
    service_config = validate_config(config)
    output_directory = validate_output_dir(output_dir)
    context = {
        "service_config": service_config,
        "output_dir": output_directory,
        "backend_only": True,
    }

    # Log the inputs
    service_name = service_config.service_info.name
    print(f"Generating Backend services for app `{service_name}`")
    print(f"\tconfig:     {config}")
    print(f"\toutput_dir: {output_dir}\n")

    # Generate the backend files and close out
    result = generate_service(**context)
    process_close(
        result=result, output_dir=output_directory, service_config=service_config
    )


@app.command()
def generate_app(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
    output_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--output-dir", "-o", help="Path to the output directory."
    ),
):
    """Generate a FastAPI backend and React frontend from the input yaml config.

    Args:
        config (Optional[str], optional): Path to the input yaml config.
            Defaults to SAMPLE_INPUT_FILE.
        output_dir (Optional[str], optional): Path to the output directory.
            Defaults to SAMPLE_OUTPUT_DIR.
    """
    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    output_directory = validate_output_dir(output_dir)
    context = {
        "service_config": service_config,
        "output_dir": output_directory,
    }

    # Log the inputs
    service_name = service_config.service_info.name
    print(f"Generating Frontend and Backend services for app `{service_name}`")
    print(f"\tconfig:     {config}")
    print(f"\toutput_dir: {output_dir}\n")

    # Generate the files and close out
    result = generate_service(**context)
    process_close(
        result=result, output_dir=output_directory, service_config=service_config
    )


if __name__ == "__main__":
    app()
