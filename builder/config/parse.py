import os
import tempfile
from typing import Any, Dict

import yaml
from pydantic.fields import FieldInfo

from builder.constants import PYTHON_DEPENDENCIES, REQUIRED_DB_ENV_VARS
from builder.models import (DatabaseTypes, DependencyConfig, FieldDefinition,
                            ModelConfig, ServiceConfig, ServiceInfo)
from builder.models.db import DBConfig, MongoDBConfig, RelationalDBConfig

# Pull output the fields from the models
FIELD_DEFINITION_FIELDS: dict[str, FieldInfo] = FieldDefinition.model_fields
MODEL_DEFINITION_FIELDS: dict[str, FieldInfo] = ModelConfig.model_fields
DEPENDENCY_DEFINITION_FIELDS: dict[str, FieldInfo] = DependencyConfig.model_fields
MODEL_DEFINITION_LIST_FIELDS: dict[str, FieldInfo] = ServiceConfig.model_fields


########################################
# Load Config                          #
########################################


def load_config(input_file: str) -> Dict:
    """Simple load config from file path. Error if cannot be found."""
    # Check if the file exists
    if not os.path.exists(input_file):
        raise ValueError(f"Config file not found at {input_file}")

    # Load the config
    with open(input_file, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    return config


########################################
# Validate Config                      #
########################################


def validate_config(config: Dict) -> None:
    """Validate the config to ensure it has the correct fields.

    Args:
        config: Dict
    Returns:
        None
    Raises:
        ValueError: If the config is invalid
    """
    # (1) Confirm top level keys in the Config
    required_top_level_keys = ["database", "models", "service"]
    if not all(key in config.keys() for key in required_top_level_keys):
        raise ValueError(
            f"Invalid top level keys in config, required keys are {required_top_level_keys}"
        )

    # (2) For each DatabaseConfig confirm fields are valid
    db_type = None
    database = config["database"]
    for field_name in database:
        if field_name == "db_type" and database[field_name] is None:
            db_type = database["db_type"]
            if db_type == DatabaseTypes.POSTGRES.value:
                for env_var in REQUIRED_DB_ENV_VARS["postgres"]:
                    if env_var not in os.environ or not os.environ[env_var]:
                        raise ValueError(
                            f"Missing required environment variable '{env_var}' for postgres"
                        )
            elif db_type == DatabaseTypes.MYSQL.value:
                for env_var in REQUIRED_DB_ENV_VARS["mysql"]:
                    if env_var not in os.environ or not os.environ[env_var]:
                        raise ValueError(
                            f"Missing required environment variable '{env_var}' for mysql"
                        )
            elif db_type == DatabaseTypes.MONGO.value:
                for env_var in REQUIRED_DB_ENV_VARS["mongo"]:
                    if env_var not in os.environ or not os.environ[env_var]:
                        raise ValueError(
                            f"Missing required environment variable '{env_var}' for mongo"
                        )
            else:
                raise ValueError(
                    f"Invalid db_type '{db_type}', allowed types are {DatabaseTypes.choices()}"
                )

    # (3) For each ModelConfig confirm fields are valid
    models = config["models"]
    model_names = [model["name"] for model in config["models"]]
    for model in models:
        if any(
            field_name not in ModelConfig.model_fields.keys()
            for field_name in model.keys()
        ):
            raise ValueError(f"Invalid field name in ModelConfig '{model['name']}'")
        for field in model["fields"]:
            # Validate the field
            if any(
                field_name not in FieldDefinition.model_fields.keys()
                for field_name in field.keys()
            ):
                raise ValueError(
                    f"Invalid field name in FieldDefinition, required fields are"
                    f"{FieldDefinition.model_fields.keys()}"
                )

            # Validate the reference (if present)
            if field.get("of_type") is not None:
                if field["of_type"] not in model_names:
                    raise ValueError(
                        f"Invalid reference '{field['of_type']}' in FieldDefinition '{field['name']}', valid references are"
                        f"{model_names}"
                    )

    # (4) For each DependencyConfig confirm fields are valid (optional so we can sub with empty list)
    dependency_defs = config.get("dependencies", [])
    for dependency in dependency_defs:
        if any(
            field_name not in DependencyConfig.model_fields.keys()
            for field_name in dependency.keys()
        ):
            raise ValueError(
                f"Invalid field name in DependencyConfig '{dependency['base']}'"
            )

    # (5) Confirm the service name is a string
    service_config = config["service"]
    service_required_keys = ["name", "version", "description"]
    if not all(key in service_config.keys() for key in service_required_keys):
        raise ValueError(
            f"Invalid top level keys in service config, required keys are {service_required_keys}"
        )


def validate_output_dir(output_dir: str):
    """Check if the output directory exists and create it if it doesn't.

    Args:
        output_dir (str): The output directory
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    return os.path.abspath(output_dir)


########################################
# Parse Model Definition               #
########################################


def parse_service_info(config: Dict[str, Any]) -> ServiceInfo:
    """Parse the service info."""
    return ServiceInfo(**config)


def parse_db_config(config: Dict[str, Any]) -> DBConfig:
    """Parse the database config."""
    if config["db_type"] == DatabaseTypes.MONGO.value:
        return MongoDBConfig(**config)
    elif config["db_type"] in [DatabaseTypes.POSTGRES.value, DatabaseTypes.MYSQL.value]:
        return RelationalDBConfig(**config)
    else:
        raise ValueError(f"Invalid db_type {config['db_type']}")


def parse_config(config) -> ServiceConfig:
    """Parse the model definition from the config.
    Args:
        config: Dict
    Returns:
        Config
    """
    # (0) Check some top level keys
    if "models" not in config:
        raise ValueError("Models not found in config")
    if "service" not in config:
        raise ValueError("Service info not found in config")
    if "database" not in config:
        raise ValueError("Database info not found in config")

    # (1) Parse the service info
    service_info = parse_service_info(config["service"])

    # (2) Parse the DB connection
    database_config = parse_db_config(config["database"])

    # (3) Parse the models
    models_config = []
    for model in config.get("models"):
        fields = []
        # Parse the fields
        if "fields" not in model:
            raise ValueError(f"Fields not found in model {model['name']}")

        for field in model["fields"]:
            fields.append(FieldDefinition(**field))
        # If no 'id' field is present, add it
        if not any(field.name == "id" for field in fields):
            print("During parsing found no id field, adding one automatically")
            fields.append(
                FieldDefinition(name="id", type="str", required=False, default=None)
            )

        models_config.append(ModelConfig(name=model["name"], fields=fields))

    # (4) Parse the dependencies (optional, yet to be implemented)
    dependencies_config = []
    if "dependencies" not in config:
        dependencies_config = [
            DependencyConfig(name=name, version=version)
            for name, version in PYTHON_DEPENDENCIES
        ]
    else:
        for dependency in config.get("dependencies", []):
            dependencies_config.append(DependencyConfig(**dependency))

    # (5) Get and validate the output directory, or create a temporary one
    output_dir = config.get("output_dir", tempfile.mkdtemp())
    output_dir = validate_output_dir(output_dir)

    # (6) Return the parsed config
    return ServiceConfig(
        output_dir=output_dir,
        service_info=service_info,
        database=database_config,
        models=models_config,
        dependencies=dependencies_config,
    )


def load_and_validate_config(input_file: str) -> ServiceConfig:
    """Load the input yaml config file.

    Args:
        input_file (str): Path to the input yaml config.

    Returns:
        Dict: Dictionary of the loaded yaml config
    """
    loaded_config: Dict = load_config(input_file=input_file)
    validate_config(loaded_config)
    return parse_config(loaded_config)
