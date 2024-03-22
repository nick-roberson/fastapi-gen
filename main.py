import os
from typing import Optional

import typer
from rich import print

from generate.constants import DEFAULT_PORT
from generate.generate import generate as generate_service
from generate.generate import generate_files
from generate.models import ServiceVersion
from generate.versions.utils import load_versions

app = typer.Typer()

# Constants
CWD: str = os.getcwd()
DEFAULT_INPUT: str = "examples/models.yaml"
DEFAULT_OUTPUT: str = f"{CWD}/output"


@app.command()
def generate(
    config: Optional[str] = typer.Option(
        DEFAULT_INPUT, "--config", "-c", help="Path to the input yaml config."
    ),
    output_dir: Optional[str] = typer.Option(
        DEFAULT_OUTPUT, "--output-dir", "-o", help="Path to the output directory."
    ),
):
    """Generate the models and services from the input yaml config."""
    # Simple validation on the input
    if not config.endswith(".yaml"):
        print(f"Input file {config} must be a yaml file")
        typer.Exit(code=1)
    if not os.path.exists(config):
        print(f"Input file {config} does not exist")
        typer.Exit(code=1)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get the absolute paths
    config_path = os.path.abspath(config)
    output_directory = os.path.abspath(output_dir)

    print(
        f"""Generating models and services with the following inputs
    Input:  {config_path}
    Output: {output_directory}
    """
    )

    # Generate those files in that directory
    result = generate_service(output_dir=output_directory, input_file=config_path)
    print(f"Generated files:")
    for key, value in result.items():
        print(f"\t{key}: {value}")

    # Auto install the dependencies using poetry
    print(f"\nInstalling dependencies using poetry ...")
    full_path = os.path.abspath(output_dir)
    os.chdir(full_path)
    os.system("poetry install")
    os.system("poetry update")
    print("Installed dependencies!")

    # Display commands for users to go and run the generated files
    print("\nRun the following commands to run the service:")
    print(f"  % cd {output_dir}")
    print(f"  % poetry run uvicorn service:app --reload --port {DEFAULT_PORT}")


@app.command()
def revert(
    version: int = typer.Option(
        None, "--version", "-v", help="The version number to revert to."
    ),
    output_dir: Optional[str] = typer.Option(
        DEFAULT_OUTPUT, "--output-dir", "-o", help="Path to the output directory."
    ),
):
    """Revert the service to a previous version."""
    print(f"""Reverting the service to version {version}, outputting to {output_dir}""")
    # Load all versions
    all_versions = load_versions()
    if not all_versions:
        print("No versions found")
        typer.Exit(code=1)

    version_names = [v.version for v in all_versions]
    if not version:
        print("Please specify a version to revert to")
        typer.Exit(code=1)
    if version not in version_names:
        print(f"Version {version} not found in {version_names}")
        typer.Exit(code=1)

    # Get the version to revert to
    version_to_revert = [v for v in all_versions if v.version == version][0]
    config = ServiceVersion(**version_to_revert.dict()).config

    result = generate_files(output_dir=output_dir, config=config, is_revert=True)
    print(f"Generated files:")
    for key, value in result.items():
        print(f"\t{key}: {value}")

    # Auto install the dependencies using poetry
    print(f"\nInstalling dependencies using poetry ...")
    full_path = os.path.abspath(output_dir)
    os.chdir(full_path)
    os.system("poetry install")
    os.system("poetry update")
    print("Installed dependencies!")

    # Display commands for users to go and run the generated files
    print("\nRun the following commands to run the service:")
    print(f"  % cd {output_dir}")
    print(f"  % poetry run uvicorn service:app --reload --port {DEFAULT_PORT}")


@app.command()
def versions():
    """List all versions of the service that have been generated."""
    # Load all versions
    all_versions = load_versions()
    # Display the versions
    print(f"Loaded {len(all_versions)} versions:")
    if not all_versions:
        print("\tNo versions found")
        return
    for version in all_versions:
        print(f"\tVersion: {version.version} - {version.created_at}")


if __name__ == "__main__":
    app()
