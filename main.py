import logging
import os
from typing import Dict, Optional

import typer

from service_builder.constants import (DEFAULT_PORT, SAMPLE_INPUT_FILE,
                                       SAMPLE_OUTPUT_DIR)
from service_builder.generate.backend.generate import generate_files
from service_builder.log import setup_logging
from service_builder.models import ServiceVersion
from service_builder.openapi.export import export_openapi
from service_builder.run import generate as generate_service
from service_builder.versions.utils import load_versions

# Initialize the logger
setup_logging()
# Initialize the typer app
app = typer.Typer()


def process_close(result: Dict, output_dir: str, service_name: str = None):
    """Show the results and close the application.

    Args:
        result (Dict): The result of the generation
        output_dir (str): The output directory
        service_name (str): The service name
    """
    # Display the generated files
    logging.info(f"Generated files:")
    for key, value in result.items():
        logging.info(f"\t{key}: {value}")

    # Display commands for users to go and run the generated files
    logging.info("\nRun the following commands to run the service:")
    logging.info(f"  % cd {output_dir}")
    logging.info(f"  % poetry run uvicorn service:app --reload --port {DEFAULT_PORT}")

    # Display the frontend commands
    if service_name:
        logging.info("\nRun the following commands to run the frontend:")
        logging.info(f"  % cd {output_dir}/{service_name}")
        logging.info(f"  % npm start")


@app.command()
def generate(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
    output_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--output-dir", "-o", help="Path to the output directory."
    ),
    service_name: Optional[str] = typer.Option(
        None, "--service-name", "-s", help="Name of the service."
    ),
    frontend_only: Optional[bool] = typer.Option(
        False, "--frontend-only", "-f", help="Generate only the front end."
    ),
    backend_only: Optional[bool] = typer.Option(
        False, "--backend-only", "-b", help="Generate only the back end."
    ),
):
    """Generate the models and services from the input yaml config."""
    # Simple validation on the input
    if not config.endswith(".yaml"):
        logging.info(f"Input file {config} must be a yaml file")
        typer.Exit(code=1)
    if not os.path.exists(config):
        logging.info(f"Input file {config} does not exist")
        typer.Exit(code=1)

    # Confirm the service name
    if not service_name:
        logging.info("Please specify a service name")
        typer.Exit(code=1)

    # Clean the service name
    service_name = service_name.lower()
    service_name = "".join(e for e in service_name if e.isalnum())

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get the absolute paths
    config_path = os.path.abspath(config)
    output_directory = os.path.abspath(output_dir)
    logging.info(
        f"""Generating models and services with the following inputs
    Input:  {config_path}
    Output: {output_directory}
    Service Name: {service_name}
    Frontend Only: {frontend_only}
    Backend Only: {backend_only}
    """
    )

    # Generate the files and close out
    result = generate_service(
        output_dir=output_directory,
        input_file=config_path,
        service_name=service_name,
        frontend_only=frontend_only,
        backend_only=backend_only,
    )
    process_close(result=result, output_dir=output_directory, service_name=service_name)


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


@app.command()
def generate_openapi(
    service_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--service-dir", "-o", help="Path to the input yaml config."
    ),
):
    """Generate the openapi file from the input yaml config."""
    # Simple verification
    if not os.path.exists(service_dir):
        logging.info(f"Output root directory {service_dir} does not exist")
        typer.Exit(code=1)

    # Get the absolute path and log args
    service_dir_abs = os.path.abspath(service_dir)
    logging.info(
        f"""Generating OpenAPI file:
    Output: {service_dir_abs}
    """
    )

    # Export the openapi file
    export_openapi(output_dir=service_dir_abs)
    logging.info("Done!")


if __name__ == "__main__":
    app()
