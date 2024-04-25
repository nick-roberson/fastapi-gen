from typing import Optional

import typer
from rich import print

from builder.app_manager import ApplicationManager
from builder.cli.utils import validate_config, validate_output_dir
from builder.constants import SAMPLE_INPUT_FILE, SAMPLE_OUTPUT_DIR

app = typer.Typer()


@app.command()
def migrate(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
    output_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--output-dir", "-o", help="Path to the output directory."
    ),
    message: Optional[str] = typer.Option(
        None, "--message", "-m", help="Message for the migration."
    ),
):
    """BETA: Create migration and apply to the database for any models that have been created"""
    print("\[red]This feature is in Beta![/red]")

    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    output_dir = validate_output_dir(output_dir)
    manager = ApplicationManager(service_config=service_config, output_dir=output_dir)

    # Log the inputs
    service_name = service_config.service_info.name
    print(f"Migrating database for app `{service_name}`")
    print(f"\tconfig:     {config}")
    print(f"\toutput_dir: {output_dir}\n")

    # Generate new migration file
    manager.create_migration(message or "New Migration")
    # Apply the migration to the database
    manager.run_migrations()

    print(f"Database migrated successfully")
    print(f"\nYou can now use this data to seed your database.")
