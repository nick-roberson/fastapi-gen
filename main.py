import logging
import os
from typing import Dict, Optional

import typer

from service_builder.config.parse import load_and_validate_config
from service_builder.constants import (DEFAULT_PORT, SAMPLE_INPUT_FILE,
                                       SAMPLE_OUTPUT_DIR)
from service_builder.generate.backend.generate import generate_files
from service_builder.log import setup_logging
from service_builder.models import ServiceVersion
from service_builder.models.configs import ServiceConfig
from service_builder.run import generate as generate_service
from service_builder.versions.utils import load_versions

# Initialize the logger
setup_logging()
# Initialize the typer app
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
        logging.info("Service name must be at least 3 characters")
        typer.Exit(code=1)
    if len(service_name) > 20:
        logging.info("Service name must be less than 20 characters")
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
        logging.info(f"Config file not found at {config_file}")
        typer.Exit(code=1)

    # Get the absolute path
    full_path = os.path.abspath(config_file)

    # Load and validate the config
    config = load_and_validate_config(full_path)
    return config


def process_close(result: Dict, output_dir: str, service_name: str = None):
    """Show the results and close the application.

    Args:
        result (Dict): The result of the generation
        output_dir (str): The output directory
        service_name (str): The service name
    """
    # Subtract the current working dir from all files in result for easier reading
    result = {
        key: [v.replace(f"{output_dir}/", "") for v in values]
        for key, values in result.items()
    }

    # Display the generated files
    logging.info(f"Generated files:")
    for key, value in result.items():
        logging.info(f"\t{key}: {value}")

    # Display commands for users to go and run the generated files
    logging.info("Run the following commands to run the service:")
    logging.info(f"\t% cd {output_dir}")
    logging.info(f"\t% poetry run uvicorn service:app --reload --port {DEFAULT_PORT}")

    # Display the frontend commands
    if service_name:
        logging.info("Run the following commands to run the frontend:")
        logging.info(f"\t% cd {output_dir}/{service_name}")
        logging.info(f"\t% npm start")


@app.command()
def validate_config(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
):
    """Validate the input yaml config."""
    validate_config(config)
    logging.info(f"Config file found at {config} is valid!")


@app.command()
def generate_typescript_app(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
    output_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--output-dir", "-o", help="Path to the output directory."
    ),
    service_name: Optional[str] = typer.Option(
        None, "--service-name", "-s", help="Name of the service."
    ),
):
    """Generate the models and services from the input yaml config."""
    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    output_directory = validate_output_dir(output_dir)
    service_name = validate_service_name(service_name)
    context = {
        "service_config": service_config,
        "output_dir": output_directory,
        "service_name": service_name,
        "frontend_only": True,
    }

    # Log the inputs
    logging.info(f"""Generating models and services with the following inputs""")
    for key, value in context.items():
        logging.info(f"\t{key}: {value}")

    # Generate the frontend files and close out
    result = generate_service(**context)
    process_close(result=result, output_dir=output_directory, service_name=service_name)


@app.command()
def generate_python_app(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
    output_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--output-dir", "-o", help="Path to the output directory."
    ),
):
    """ "Generate the models and services from the input yaml config."""
    # Validate the input and get absolute paths
    service_config = validate_config(config)
    output_directory = validate_output_dir(output_dir)
    context = {
        "service_config": service_config,
        "output_dir": output_directory,
        "backend_only": True,
    }

    # Log the inputs
    logging.info(f"""Generating models and services with the following inputs""")
    for key, value in context.items():
        logging.info(f"\t{key}: {value}")

    # Generate the backend files and close out
    result = generate_service(**context)
    process_close(result=result, output_dir=output_directory)


@app.command()
def generate_app(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
    output_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--output-dir", "-o", help="Path to the output directory."
    ),
    service_name: Optional[str] = typer.Option(
        None, "--service-name", "-s", help="Name of the service."
    ),
):
    """Generate the models and services from the input yaml config."""
    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    output_directory = validate_output_dir(output_dir)
    service_name = validate_service_name(service_name)
    context = {
        "service_config": service_config,
        "output_dir": output_directory,
        "service_name": service_name,
    }

    # Log the inputs
    logging.info(f"""Generating models and services with the following inputs""")
    for key, value in context.items():
        logging.info(f"\t{key}: {value}")

    # Generate the files and close out
    result = generate_service(**context)
    process_close(result=result, output_dir=output_directory, service_name=service_name)


# TODO: Rewrite this function
@app.command()
def revert(
    version: int = typer.Option(
        None, "--version", "-v", help="The version number to revert to."
    ),
    output_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--output-dir", "-o", help="Path to the output directory."
    ),
):
    """Revert the service to a previous version."""
    logging.info(
        f"""Reverting the service to version {version}, outputting to {output_dir}"""
    )

    # Load all versions
    all_versions = load_versions()
    if not all_versions:
        logging.info("No versions found")
        typer.Exit(code=1)

    # Check if the version exists
    version_names = [v.version for v in all_versions]
    if not version:
        logging.info("Please specify a version to revert to")
        typer.Exit(code=1)
    if version not in version_names:
        logging.info(f"Version {version} not found in {version_names}")
        typer.Exit(code=1)

    # Get the version to revert to
    version_to_revert = [v for v in all_versions if v.version == version][0]
    config = ServiceVersion(**version_to_revert.dict()).config

    # Generate the files and close out
    output_directory = os.path.abspath(output_dir)
    result = generate_files(output_dir=output_directory, config=config, is_revert=True)
    process_close(result=result, output_dir=output_directory)


@app.command()
def versions():
    """List all versions of the service that have been generated."""
    # Load all versions
    all_versions = load_versions()
    # Display the versions
    logging.info(f"Loaded {len(all_versions)} versions:")
    if not all_versions:
        logging.info("\tNo versions found")
        return
    for version in all_versions:
        logging.info(f"\tVersion: {version.version} - {version.created_at}")


if __name__ == "__main__":
    app()
