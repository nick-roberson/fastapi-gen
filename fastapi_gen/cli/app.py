from typing import Optional

import typer
from rich import print

from fastapi_gen.app_manager import ApplicationManager
from fastapi_gen.cli.utils import process_close, validate_config
from fastapi_gen.constants import TEST_MYSQL_CONFIG

app = typer.Typer()


@app.command()
def create(
    config: Optional[str] = typer.Option(
        TEST_MYSQL_CONFIG, "--config", "-c", help="Path to the input yaml config."
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
            Defaults to TEST_MYSQL_CONFIG.
        frontend_only (bool, optional): Generate only the frontend code.
            Defaults to False.
        backend_only (bool, optional): Generate only the backend code.
            Defaults to False.
    """
    # Check for invalid inputs
    if frontend_only and backend_only:
        raise ValueError(
            "Cannot regenerate both frontend and backend at the same time."
        )

    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)

    # Log the inputs
    service_name = service_config.service_info.name
    print(f"Generating Frontend and Backend services for app `{service_name}`")
    print(f"\tconfig:           {config}")
    print(f"\tfrontend_only:    {frontend_only}")
    print(f"\tbackend_only:     {backend_only}\n")

    # Generate the files and close out
    manager = ApplicationManager(config=service_config)
    created_files = manager.generate(
        frontend_only=frontend_only, backend_only=backend_only
    )
    process_close(
        result=created_files,
        config=service_config,
        config_path=config,
    )


@app.command()
def reload(
    config: Optional[str] = typer.Option(
        TEST_MYSQL_CONFIG, "--config", "-c", help="Path to the input yaml config."
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
            Defaults to TEST_MYSQL_CONFIG.
        frontend_only (bool, optional): Regenerate only the frontend code.
            Defaults to False.
        backend_only (bool, optional): Regenerate only the backend code.
            Defaults to False.
    """
    # Check for invalid inputs
    if frontend_only and backend_only:
        raise ValueError(
            "Cannot regenerate both frontend and backend at the same time."
        )

    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    manager = ApplicationManager(config=service_config)

    # Regenerate the files and close out
    regenerated_files = manager.regenerate(
        frontend_only=frontend_only, backend_only=backend_only
    )
    process_close(
        result=regenerated_files,
        config=service_config,
        config_path=config,
    )


@app.command()
def run_frontend(
    config: Optional[str] = typer.Option(
        TEST_MYSQL_CONFIG, "--config", "-c", help="Path to the input yaml config."
    ),
):
    """Run the React frontend from the input yaml config.

    Args:
        config (Optional[str], optional): Path to the input yaml config.
            Defaults to TEST_MYSQL_CONFIG.
        output_dir (Optional[str], optional): Path to the output directory.
            Defaults to SAMPLE_OUTPUT_DIR.
    """
    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    manager = ApplicationManager(config=service_config)

    # Log the inputs
    service_name = service_config.service_info.name
    print(f"Running Frontend and Backend services for app `{service_name}`")
    print(f"\tconfig:           {config}")

    # Run the application
    manager.run_frontend()


@app.command()
def run_backend(
    config: Optional[str] = typer.Option(
        TEST_MYSQL_CONFIG, "--config", "-c", help="Path to the input yaml config."
    ),
):
    """Run the FastAPI backend from the input yaml config.

    Args:
        config (Optional[str], optional): Path to the input yaml config.
            Defaults to TEST_MYSQL_CONFIG.
    """
    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    manager = ApplicationManager(config=service_config)

    # Log the inputs
    service_name = service_config.service_info.name
    print(f"Running Frontend and Backend services for app `{service_name}`")
    print(f"\tconfig:           {config}")

    # Run the application
    manager.run_backend()
