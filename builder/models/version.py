import os

import yaml
from pydantic import BaseModel

from builder.models import ServiceConfig


class ConfigVersion(BaseModel):
    """Version information for the configuration file."""

    # Version Id
    version: str

    # Service configuration
    service_config: ServiceConfig

    # Configuration file path
    config_file: str

    # Creation date
    created_at: str

    def to_file(self, file_path: str):
        """Writes config to a YAML file"""
        # If the directory does not exist, create it
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Obfuscate the database password
        config_dict = self.dict()
        if self.database.db_type in ["mysql", "postgres"]:
            config_dict["database"]["config"]["password"] = "********"
            config_dict["database"]["config"]["host"] = "********"
        elif self.database.db_type == "mongo":
            config_dict["database"]["config"]["db_uri"] = "********"

        # Write the config to the file
        with open(file_path, "w") as file:
            yaml.dump(config_dict, file)

    def from_file(file_path: str):
        """Reads config from a YAML file"""
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Config file not found at {file_path}")
        # Read the config from the file
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
            return ConfigVersion(**data)
