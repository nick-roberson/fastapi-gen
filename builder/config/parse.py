import os
from typing import Dict

import yaml
from pydantic.fields import FieldInfo

from builder.constants import PYTHON_DEPENDENCIES, REQUIRED_DB_ENV_VARS
from builder.models import (DatabaseConfig, DatabaseTypes, DependencyConfig,
                            FieldDefinition, ModelConfig, ServiceConfig,
                            ServiceInfo)

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


def validate_field(field: FieldDefinition) -> None:
    field_info = FIELD_DEFINITION_FIELDS.get(field.name)
    if field_info is None:
        raise ValueError(f"Invalid field name '{field.name}' in FieldDefinition")


def validate_dependencies(dependency: DependencyConfig) -> None:
    for field_name in dependency:
        if field_name not in DEPENDENCY_DEFINITION_FIELDS.keys():
            raise ValueError(
                f"Invalid field name '{field_name}' in DependencyConfig {dependency['base']}"
            )


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
    database = config["database"]
    for field_name in database:
        if field_name not in DatabaseConfig.model_fields.keys():
            raise ValueError(f"Invalid field name in DatabaseConfig '{field_name}'")
        if (
            field_name == "db_type"
            and database[field_name] not in DatabaseTypes.choices()
        ):
            raise ValueError(
                f"Invalid db_type '{database[field_name]}', allowed types are {DatabaseConfig.db_type_choices}"
            )

        # Check the db_type is present and all vars are present
        if field_name == "db_type" and database[field_name] is None:
            db_type = database["db_type"]
            if db_type == DatabaseTypes.postgres.value:
                for env_var in REQUIRED_DB_ENV_VARS["postgres"]:
                    if env_var not in os.environ or not os.environ[env_var]:
                        raise ValueError(
                            f"Missing required environment variable '{env_var}' for postgres"
                        )
            elif db_type == DatabaseTypes.mysql.value:
                for env_var in REQUIRED_DB_ENV_VARS["mysql"]:
                    if env_var not in os.environ or not os.environ[env_var]:
                        raise ValueError(
                            f"Missing required environment variable '{env_var}' for mysql"
                        )
            elif db_type == DatabaseTypes.mongo.value:
                for env_var in REQUIRED_DB_ENV_VARS["mongo"]:
                    if env_var not in os.environ or not os.environ[env_var]:
                        raise ValueError(
                            f"Missing required environment variable '{env_var}' for mongo"
                        )
            else:
                raise ValueError(
                    f"Invalid db_type '{db_type}', allowed types are {DatabaseConfig.db_type_choices}"
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


########################################
# Parse Model Definition               #
########################################


def parse_config(config) -> ServiceConfig:
    """Parse the model definition from the config.
    Args:
        config: Dict
    Returns:
        Config
    """
    # (1) Parse the service info
    service_info = ServiceInfo(**config["service"])

    # (2) Parse the DB connection
    database_config = DatabaseConfig(**config["database"])

    # (3) Parse the models
    models_config = []
    for model in config.get("models", []):
        fields = []
        # Parse the fields
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

    return ServiceConfig(
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
