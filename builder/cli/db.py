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
    """BETA: Create migration and apply to the database for any models that have been created

    Args:
        config (Optional[str], optional): Path to the input yaml config.
            Defaults to SAMPLE_INPUT_FILE.
        output_dir (Optional[str], optional): Path to the output directory.
            Defaults to SAMPLE_OUTPUT_DIR.
        message (Optional[str], optional): Message for the migration.

    Example:
        export DB_NAME=restaurants && poetry run python main.py db migrate \
            --config example/alembic/restaurant.yaml \
            --output-dir example/alembic/output
    """
    print(
        "[red]This feature is in beta and may not work as expected. Please report any issues on GitHub.[/red]"
    )

    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    output_dir = validate_output_dir(output_dir)
    manager = ApplicationManager(service_config=service_config, output_dir=output_dir)

    # Generate new migration file and apply to the database
    manager.create_migration(message or "New Migration")
    manager.run_migrations()

    print(f"Database migrated successfully")
    print(f"\nYou can now use this data to seed your database.")


@app.command()
def revert(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
    output_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--output-dir", "-o", help="Path to the output directory."
    ),
    revision: Optional[str] = typer.Option(
        None, "--revision", "-r", help="Revision to revert to."
    ),
):
    """BETA: Revert the database to a previous revision

    Args:
        config (Optional[str], optional): Path to the input yaml config.
            Defaults to SAMPLE_INPUT_FILE.
        output_dir (Optional[str], optional): Path to the output directory.
            Defaults to SAMPLE_OUTPUT_DIR.
        revision (Optional[str], optional): Revision to revert to.

    Example:
        export DB_NAME=restaurants && poetry run python main.py revert list \
            --config example/alembic/restaurant.yaml \
            --output-dir example/alembic/output
    """
    print(
        "[red]This feature is in beta and may not work as expected. Please report any issues on GitHub.[/red]"
    )

    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    output_dir = validate_output_dir(output_dir)
    manager = ApplicationManager(service_config=service_config, output_dir=output_dir)

    # Revert the database to the specified revision
    manager.revert_migration(revision)

    print(f"Database reverted successfully")
    print(f"\nYou can now use this data to seed your database.")


@app.command()
def list(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
    output_dir: Optional[str] = typer.Option(
        SAMPLE_OUTPUT_DIR, "--output-dir", "-o", help="Path to the output directory."
    ),
):
    """BETA: List all migrations

    Args:
        config (Optional[str], optional): Path to the input yaml config.
            Defaults to SAMPLE_INPUT_FILE.
        output_dir (Optional[str], optional): Path to the output directory.
            Defaults to SAMPLE_OUTPUT_DIR.

    Example:
        export DB_NAME=restaurants && poetry run python main.py db list \
            --config example/alembic/restaurant.yaml \
            --output-dir example/alembic/output
    """
    print(
        "[red]This feature is in beta and may not work as expected. Please report any issues on GitHub.[/red]"
    )

    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    output_dir = validate_output_dir(output_dir)
    manager = ApplicationManager(service_config=service_config, output_dir=output_dir)

    # List all migrations
    manager.get_migrations()

    print(f"List of all migrations")
    print(f"\nYou can now use this data to seed your database.")
