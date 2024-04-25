import typer

from builder.cli.app import app as create_app
from builder.cli.config import app as create_config
from builder.cli.data import app as create_test_data

# Initialize the main Typer application
app = typer.Typer()

# Add subcommands for creating applications
app.add_typer(
    create_app,
    name="app",
    help="Create a FastAPI backend and/or React frontend from an input yaml config.",
)
# Add subcommands for configs
app.add_typer(
    create_config,
    name="config",
    help=(
        "Interactively create a configuration file that can then be used for generating a FastAPI backend and "
        "React frontend."
    ),
)
# Add subcommands for test data
app.add_typer(
    create_test_data,
    name="data",
    help="Generate fake data for the service using Faker (https://faker.readthedocs.io/).",
)


def run():
    """Run the CLI application."""
    app()


if __name__ == "__main__":
    run()
