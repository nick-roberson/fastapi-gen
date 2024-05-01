from typing import Optional

import typer
from rich import print

from builder.cli.utils import validate_config
from builder.constants import SAMPLE_INPUT_FILE, SAMPLE_OUTPUT_DIR
from builder.test_data.create_fake_data import create_fake_data

app = typer.Typer()


@app.command()
def create(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input yaml config."
    ),
):
    """Generate fake data for the service"""
    # Validate the inputs, get absolute paths, clean the service name, build the context
    service_config = validate_config(config)
    # Log the inputs
    service_name = service_config.service_info.name
    print(f"Generating fake data for app `{service_name}`")
    print(f"\tconfig:     {config}")

    # Generate the fake data and close out
    result = create_fake_data(confg=service_config)
    print(f"Generated fake data at")
    for model_name, file_path in result.items():
        print(f"\t{model_name}: {file_path}")
    print(f"\nYou can now use this data to seed your database.")
