from typing import Optional

import typer
from rich import print

from builder.cli.utils import validate_config
from builder.constants import SAMPLE_INPUT_FILE
from builder.test_data.create_fake_data import create_fake_data

app = typer.Typer()


@app.command()
def create(
    config: Optional[str] = typer.Option(
        SAMPLE_INPUT_FILE, "--config", "-c", help="Path to the input YAML config."
    )
):
    """
    Generate fake data for the service based on a specified YAML configuration file.

    Args:
        config (str, optional): Path to the input YAML configuration file.
            Defaults to SAMPLE_INPUT_FILE.
    """
    # Validate and process the configuration file
    service_config = validate_config(config)

    # Retrieve and log service name from the configuration
    service_name = service_config.service_info.name
    print(f"Generating fake data for app `{service_name}`")
    print(f"\tconfig:     {config}")

    # Generate fake data as per the configuration and log the output
    result = create_fake_data(config=service_config)
    print("Generated fake data at:")
    for model_name, file_path in result.items():
        print(f"\t{model_name}: {file_path}")
    print("\nYou can now use this data to seed your database.")
