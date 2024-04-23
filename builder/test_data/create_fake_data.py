import json
import os
from typing import Dict

from rich import print

from builder.models.configs import ServiceConfig

DATA_DIR: str = "data"


def create_fake_data(service_config: ServiceConfig, output_dir: str) -> Dict:
    """Create fake data for the service

    Args:
        service_config (ServiceConfig): Service configuration
        output_dir (str): Output directory for the fake data
    Returns:
        Dict: Dictionary of model names and their corresponding fake data file paths
    """
    # Create the output directory and data directory
    data_dir = os.path.join(output_dir, DATA_DIR)
    os.makedirs(data_dir, exist_ok=True)
    print(f"Creating fake data at {data_dir}")

    # Get model list and create fake data
    models = service_config.models
    data = {
        model.name: [model.create_fake_data() for _ in range(5)] for model in models
    }

    # Output the fake data each to a JSON file
    result_files = {}
    for model_name, model_data in data.items():
        output_file = os.path.join(data_dir, f"{model_name}.json")
        print(f"Creating fake data for {model_name} at {output_file}")
        with open(output_file, "w") as f:
            json.dump(model_data, f, indent=2)
        result_files[model_name] = output_file

    # Return the output directory of the fake data
    return result_files
