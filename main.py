import json
import os
from typing import Dict, Optional

import typer
from rich import print

from builder.cli.config_builder import create_config
from builder.config.parse import load_and_validate_config
from builder.constants import (DEFAULT_PORT, SAMPLE_INPUT_FILE,
                               SAMPLE_OUTPUT_DIR)
from builder.generate.backend.generator import BackendGenerator
from builder.generate.frontend.generator import FrontendGenerator
from builder.models.configs import ServiceConfig
from builder.run import ApplicationManager
from builder.test_data.create_fake_data import create_fake_data

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
    code_dir = "backend"
    service_name = service_config.service_info.name

    # Display the generated files
    print(f"\nGenerated files:")
    print(json.dumps(result, indent=4))

    # Display commands for users to go and run the generated files
    print("")
    print("Run Backend (Poetry):")
    print(f"   % cd {output_dir}/{code_dir}")
    print(f"   % poetry install && poetry update")
    print(f"   % poetry run uvicorn service:app --reload --port {DEFAULT_PORT}")

    print("")
    print("Run Backend (Docker) (Make sure to fill out the generated .env file!):")
    print(f"   % cd {output_dir}/{code_dir}")
    print(f"   % docker build -t {service_name} .")
    print(f"   % docker run -p {DEFAULT_PORT}:{DEFAULT_PORT} {service_name}")

    # Display the frontend commands
    print("")
    print("Run Frontend (NPM):")
    print(f"   % cd {output_dir}/{service_name}")
    print(f"   % npm install && npm run start")


@app.command()
def generate(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
    output_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--output-dir", "-o", help="Path to the output directory."
    ),
    frontend_only: bool = typer.Option(
        False, "--frontend-only", "-f", help="Generate only the frontend code."
    ),
    backend_only: bool = typer.Option(
        False, "--backend-only", "-b", help="Generate only the backend code."
    ),
):
    """Generate a FastAPI backend and React frontend from the input yaml config.

    Args:
        config (Optional[str], optional): Path to the input yaml config.
            Defaults to SAMPLE_INPUT_FILE.
        output_dir (Optional[str], optional): Path to the output directory.
            Defaults to SAMPLE_OUTPUT_DIR.
        frontend_only (bool, optional): Generate only the frontend code.
            Defaults to False.
        backend_only (bool, optional): Generate only the backend code.
            Defaults to False.
    """
    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    output_dir = validate_output_dir(output_dir)

    # Log the inputs
    service_name = service_config.service_info.name
    print(f"Generating Frontend and Backend services for app `{service_name}`")
    print(f"\tconfig:           {config}")
    print(f"\toutput_dir:       {output_dir}")
    print(f"\tfrontend_only:    {frontend_only}")
    print(f"\tbackend_only:     {backend_only}\n")

    # Generate the files and close out
    manager = ApplicationManager(service_config=service_config, output_dir=output_dir)
    result = manager.generate(frontend_only=frontend_only, backend_only=backend_only)
    process_close(result=result, output_dir=output_dir, service_config=service_config)


@app.command()
def regenerate(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
    output_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--output-dir", "-o", help="Path to the output directory."
    ),
    frontend_only: bool = typer.Option(
        False, "--frontend-only", "-f", help="Regenerate only the frontend code."
    ),
    backend_only: bool = typer.Option(
        False, "--backend-only", "-b", help="Regenerate only the backend code."
    ),
):
    """Just regenerate the frontend or backend templates, do not recreate the application.

    Args:
        config (Optional[str], optional): Path to the input yaml config.
            Defaults to SAMPLE_INPUT_FILE.
        output_dir (Optional[str], optional): Path to the output directory.
            Defaults to SAMPLE_OUTPUT_DIR.
        frontend_only (bool, optional): Regenerate only the frontend code.
            Defaults to False.
        backend_only (bool, optional): Regenerate only the backend code.
            Defaults to False.
    """
    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    output_dir = validate_output_dir(output_dir)

    if frontend_only and not backend_only:
        # Create frontend generator
        frontend_generator = FrontendGenerator(
            config=service_config, output_dir=output_dir
        )

        # Recreate the frontend templates
        created_files = frontend_generator.generate_templated_components()
        print(f"Regenerated frontend templates!")
        print(f"Created files: {json.dumps(created_files, indent=4)}")

    elif backend_only and not frontend_only:
        # Create backend generator
        backend_generator = BackendGenerator(
            config=service_config, output_dir=output_dir
        )

        # Recreate the backend templates
        created_files = backend_generator.generate_templated_components()
        print(f"Regenerated backend templates!")
        print(f"Created files: {json.dumps(created_files, indent=4)}")

    else:
        # Regenerate both frontend and backend
        manager = ApplicationManager(
            service_config=service_config, output_dir=output_dir
        )
        result = manager.regenerate(
            frontend_only=frontend_only, backend_only=backend_only
        )
        process_close(
            result=result, output_dir=output_dir, service_config=service_config
        )


@app.command()
def test_data(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
    output_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--output-dir", "-o", help="Path to the output directory."
    ),
):
    """Generate fake data for the service"""
    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    output_dir = validate_output_dir(output_dir)
    context = {
        "service_config": service_config,
        "output_dir": output_dir,
    }

    # Log the inputs
    service_name = service_config.service_info.name
    print(f"Generating fake data for app `{service_name}`")
    print(f"\tconfig:     {config}")
    print(f"\toutput_dir: {output_dir}\n")

    # Generate the fake data and close out
    result = create_fake_data(**context)
    print(f"Generated fake data at")
    for model_name, file_path in result.items():
        print(f"\t{model_name}: {file_path}")
    print(f"\nYou can now use this data to seed your database.")


@app.command()
def create(
    output_dir: Optional[str] = typer.Option(
        None, "--output-dir", "-o", help="Path to the output directory."
    )
):
    """Create a new configuration file interactively.

    Args:
        output_dir (Optional[str], optional): Path to the output directory.
            Defaults to SAMPLE_OUTPUT_DIR.
    """
    # Print in red color
    print("[red]This feature is in Beta![/red]")

    # Validate that the output directory exists
    if output_dir is None:
        raise typer.BadParameter("Output directory is required")
    output_dir = validate_output_dir(output_dir)

    # Create Configuration file interactively
    print(f"Creating a new configuration file interactively!")
    config_path = create_config(output_dir=output_dir)
    print(f"Configuration file created at {config_path}")

    # Optionally ask the user if they want to validate the config
    validate = input("Do you want to validate the config? (y/n): ")
    if validate.lower() == "y":
        try:
            validate_config(config_path)
            print(f"Config validated successfully!")
        except Exception as e:
            print(f"Config validation failed: {e}")
            print("See the example in the README.md file for reference")
    else:
        print(
            "Please validate the config before you try generating the application! See the example in the README.md "
            "file for reference"
        )


if __name__ == "__main__":
    """Run the CLI application."""
    app()
