import os
from typing import Dict, Tuple

import yaml
from pydantic.fields import FieldInfo

from service_builder.generate.models import (Config, DatabaseConfig,
                                             DatabaseTypes, DependencyConfig,
                                             FieldDefinition, ModelConfig)

# Pull output the fields from the models
FIELD_DEFINITION_FIELDS: dict[str, FieldInfo] = FieldDefinition.model_fields
MODEL_DEFINITION_FIELDS: dict[str, FieldInfo] = ModelConfig.model_fields
DEPENDENCY_DEFINITION_FIELDS: dict[str, FieldInfo] = DependencyConfig.model_fields
MODEL_DEFINITION_LIST_FIELDS: dict[str, FieldInfo] = Config.model_fields


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
        raise ValueError(f"Invalid field name `{field.name}` in FieldDefinition")


def validate_dependencies(dependency: DependencyConfig) -> None:
    for field_name in dependency:
        if field_name not in DEPENDENCY_DEFINITION_FIELDS.keys():
            raise ValueError(
                f"Invalid field name `{field_name}` in DependencyConfig {dependency['base']}"
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
    required_top_level_keys = ["database", "models"]
    if not all(key in config.keys() for key in required_top_level_keys):
        raise ValueError(
            f"Invalid top level keys in config, required keys are {required_top_level_keys}"
        )

    # (2) For each DatabaseConfig confirm fields are valid
    database = config["database"]
    for field_name in database:
        if field_name not in DatabaseConfig.model_fields.keys():
            raise ValueError(f"Invalid field name in DatabaseConfig `{field_name}`")
        if (
            field_name == "db_type"
            and database[field_name] not in DatabaseTypes.choices()
        ):
            raise ValueError(
                f"Invalid db_type `{database[field_name]}`, allowed types are {DatabaseConfig.db_type_choices}"
            )

    # (3) For each ModelConfig confirm fields are valid
    models = config["models"]
    model_names = [model["name"] for model in config["models"]]
    for model in models:
        if any(
            field_name not in ModelConfig.model_fields.keys()
            for field_name in model.keys()
        ):
            raise ValueError(f"Invalid field name in ModelConfig `{model['name']}`")
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
                        f"Invalid reference `{field['of_type']}` in FieldDefinition `{field['name']}`, valid references are"
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
                f"Invalid field name in DependencyConfig `{dependency['base']}`"
            )


########################################
# Parse Model Definition               #
########################################


def parse_config(config) -> Config:
    """Parse the model definition from the config.
    Args:
        config: Dict
    Returns:
        Config
    """
    # (1) Parse the DB connection
    database_config = DatabaseConfig(**config["database"])

    # (2) Parse the models
    models_config = []
    for model in config.get("models", []):
        fields = []

        # Parse the fields
        for field in model["fields"]:
            fields.append(FieldDefinition(**field))

        # If no `id` field is present, add it
        if not any(field.name == "id" for field in fields):
            print("During parsing found no id field, adding one automatically")
            fields.append(
                FieldDefinition(name="id", type="str", required=False, default=None)
            )

        models_config.append(ModelConfig(name=model["name"], fields=fields))

    # (3) Parse the dependencies (optional, yet to be implemented)
    dependencies_config = []
    for dependency in config.get("dependencies", []):
        dependencies_config.append(DependencyConfig(**dependency))

    return Config(
        database=database_config, models=models_config, dependencies=dependencies_config
    )
