from typing import Optional

import typer
from rich import print

from builder.app_manager import ApplicationManager
from builder.cli.utils import validate_config
from builder.constants import SAMPLE_INPUT_FILE

app = typer.Typer()


def _get_manager(config: str) -> ApplicationManager:
    """Get the ApplicationManager object from the config file."""
    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    manager = ApplicationManager(config=service_config)

    # If the db_type is "mongo" show an error
    if service_config.database.db_type == "mongo":
        print(
            "[red]MongoDB is not supported for migrations. "
            "Please use a relational database like MySQL or PostgreSQL.[/red]"
        )
        typer.Exit(code=1)

    return manager


@app.command()
def migrate(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
    message: Optional[str] = typer.Option(
        None, "--message", "-m", help="Message for the migration."
    ),
):
    """ Create migration and apply to the database for any models that have been created

    Args:
        config (Optional[str], optional): Path to the input yaml config.
            Defaults to SAMPLE_INPUT_FILE.
        message (Optional[str], optional): Message for the migration.

    Example:
        export DB_NAME=restaurants && poetry run python main.py db migrate \
            --config example/alembic/restaurant.yaml \
            --output-dir example/alembic/output
    """
    # Get the ApplicationManager object from the config file
    manager = _get_manager(config)

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
    revision: Optional[str] = typer.Option(
        None, "--revision", "-r", help="Revision to revert to."
    ),
):
    """ Revert the database to a previous revision

    Args:
        config (Optional[str], optional): Path to the input yaml config.
            Defaults to SAMPLE_INPUT_FILE.
        revision (Optional[str], optional): Revision to revert to.

    Example:
        export DB_NAME=restaurants && poetry run python main.py revert list \
            --config example/alembic/restaurant.yaml \
            --output-dir example/alembic/output
    """
    # Get the ApplicationManager object from the config file
    manager = _get_manager(config)

    # Revert the database to the specified revision
    manager.revert_migration(revision)

    print(f"Database reverted successfully")
    print(f"\nYou can now use this data to seed your database.")


@app.command()
def list(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
):
    """ List all migrations

    Args:
        config (Optional[str], optional): Path to the input yaml config.
            Defaults to SAMPLE_INPUT_FILE.

    Example:
        export DB_NAME=restaurants && poetry run python main.py db list \
            --config example/alembic/restaurant.yaml \
            --output-dir example/alembic/output
    """
    # Get the ApplicationManager object from the config file
    manager = _get_manager(config)

    # List all migrations
    manager.show_migrations()

    print(f"List of all migrations")
    print(f"\nYou can now use this data to seed your database.")
