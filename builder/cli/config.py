import os
from typing import Optional

import typer
import yaml
from rich import print

from builder.cli.utils import validate_config, validate_output_dir

app = typer.Typer()


def input_field(field_name, required=True, default=None):
    """Get user input for a field.

    Args:
        field_name (str): The name of the field.
        required (bool): If the field is required.
        default: The default value for the field.
    Returns:
        str: The user input value.
    """
    while True:
        value = input(
            f"Enter {field_name} ({'required' if required else 'optional'}, default: {default}): "
        )
        if value:
            return value
        elif not required or default is not None:
            return default
        else:
            print(f"{field_name} is required. Please enter a value.")


def create_config(output_dir: str) -> str:
    """Create a configuration file for the service using user input.

    Args:
        output_dir (str): The output directory for the configuration file.
    Returns:
        str: The path to the configuration file.
    """
    config = {
        # Get service information
        "service": {
            "name": input_field("service name", required=False, default="my_service"),
            "email": input_field("service email", required=False, default=""),
            "version": input_field("service version", required=False, default="0.1.0"),
            "description": input_field(
                "service description", required=False, default="A service description."
            ),
        },
        # Get database information
        "database": {
            "db_type": input_field("database type", required=True, default="mysql"),
            "host_env": input_field(
                "database host environment variable", required=True, default="DB_HOST"
            ),
            "port_env": input_field(
                "database port environment variable", required=True, default="DB_PORT"
            ),
            "user_env": input_field(
                "database user environment variable", required=True, default="DB_USER"
            ),
            "password_env": input_field(
                "database password environment variable",
                required=True,
                default="DB_PASSWORD",
            ),
            "db_name_env": input_field(
                "database name environment variable", required=True, default="DB_NAME"
            ),
        },
        "models": [],
    }

    # Get model information
    model_count = int(input("How many models would you like to define? "))
    for _ in range(model_count):
        model_name = input_field("model name")
        field_count = int(input(f"How many fields for the {model_name} model? "))
        fields = []
        for __ in range(field_count):
            field = {
                "name": input_field("Field name (ex: name, age, etc.)"),
                "type": input_field("Field type (ex: string, int, list, etc.)"),
                "required": input_field(
                    "Field required (True/False)", default="False"
                ).lower()
                in ["true", "1", "t", "yes", "y"],
                "default": input_field("Field default", required=False),
                "description": input_field(
                    "Field description", required=False, default=""
                ),
            }

            # Add the field to the model
            fields.append(field)
            print(f"Field {field['name']} added to model {model_name}.\n")

        config["models"].append({"name": model_name, "fields": fields})

    # Write the configuration to a file
    config_file = os.path.join(output_dir, "config.yaml")
    with open(config_file, "w") as file:
        yaml.dump(config, file, sort_keys=False)

    # Return the path to the configuration file
    return config_file


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
