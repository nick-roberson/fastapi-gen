import os
from typing import Dict

from generate.backend.generate import generate_files, lint_code
from generate.backend.openapi.export_openapi import export_openapi
from generate.backend.parse import load_config, parse_config, validate_config
from generate.frontend.generate import generate_frontend
from generate.models import Config


def generate_back(output_dir: str, input_file: str) -> Dict:
    """Generate the models and services from the input yaml config.

    Args:
        output_dir (str): Output directory
        input_file (str): Path to the input yaml config.

    Returns:
        Dict: Dictionary of the generated files
    """
    # Load and validate the config
    print(f"Loading and validating the config ...")
    loaded_config = load_config(input_file=input_file)
    validate_config(loaded_config)
    config = parse_config(loaded_config)
    print("Loaded and validated the config!")

    # Generate the files
    print(f"\nGenerating models and services ...")
    result = generate_files(output_dir, config, is_revert=False)
    print("Generated models and services!")

    # Install the dependencies
    print(f"\nInstalling dependencies using poetry ...")
    full_path = os.path.abspath(output_dir)
    os.chdir(full_path)
    os.system("poetry install")
    os.system("poetry update")
    print("Installed dependencies!")

    # Export the OpenAPI JSON
    print(f"\nExporting OpenAPI JSON ...")
    export_openapi(
        application_name="service:app",
        application_dir=output_dir,
        output_file=f"{output_dir}/openapi.json",
    )
    print("Exported OpenAPI JSON!")

    # Lint the code
    print(f"\nLinting the code ...")
    lint_code(output_dir)
    print("Linted the code!")

    return result


def generate_front(output_dir: str):
    """Generates a typescript / react front end from scratch."""
    generate_frontend(output_dir)


def generate(input_file: str, output_dir: str):
    """Generate the models and services from the input yaml config."""
    # Generate the backend
    result = generate_back(output_dir, input_file)

    # Generate the frontend
    generate_front(output_dir)

    return result
