import typer

from fastapi_gen.cli.app import app as app_cli
from fastapi_gen.cli.config import app as config_cli
from fastapi_gen.cli.data import app as data_cli
from fastapi_gen.cli.db import app as db_cli

# Initialize the main Typer application
app = typer.Typer()

# Add subcommands for creating applications
app.add_typer(
    app_cli,
    name="app",
    help="Create a FastAPI backend and/or React frontend from an input yaml config.",
)
# Add subcommands for database migrations
app.add_typer(
    db_cli,
    name="db",
    help="Create and apply migrations to the database for any models that have been created.",
)
# Add subcommands for configs
app.add_typer(
    config_cli,
    name="config",
    help=(
        "Interactively create a configuration file that can then be used for generating a FastAPI backend and "
        "React frontend."
    ),
)
# Add subcommands for test data
app.add_typer(
    data_cli,
    name="data",
    help="Generate fake data for the service using Faker (https://faker.readthedocs.io/).",
)


def run():
    """Run the CLI application."""
    app()


if __name__ == "__main__":
    run()
