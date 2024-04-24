import json
from typing import Optional

import typer
from rich import print

from builder.app_manager import ApplicationManager
from builder.cli.utils import (process_close, validate_config,
                               validate_output_dir)
from builder.constants import SAMPLE_INPUT_FILE, SAMPLE_OUTPUT_DIR
from builder.generate.backend.generator import BackendGenerator
from builder.generate.frontend.generator import FrontendGenerator

app = typer.Typer()


@app.command()
def create(
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
def reload(
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
