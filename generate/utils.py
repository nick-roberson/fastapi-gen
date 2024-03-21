import os
from typing import Dict, Tuple

import yaml
from pydantic.fields import FieldInfo

from generate.models import (DatabaseConfig, DependencyDefinition,
                             FieldDefinition, ModelDefinition,
                             ModelDefinitionList)

# Pull output the fields from the models
FIELD_DEFINITION_FIELDS: dict[str, FieldInfo] = FieldDefinition.model_fields
MODEL_DEFINITION_FIELDS: dict[str, FieldInfo] = ModelDefinition.model_fields
DEPENDENCY_DEFINITION_FIELDS: dict[str, FieldInfo] = DependencyDefinition.model_fields
MODEL_DEFINITION_LIST_FIELDS: dict[str, FieldInfo] = ModelDefinitionList.model_fields


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


def validate_dependencies(dependency: DependencyDefinition) -> None:
    for field_name in dependency:
        if field_name not in DEPENDENCY_DEFINITION_FIELDS.keys():
            raise ValueError(
                f"Invalid field name `{field_name}` in DependencyDefinition {dependency['base']}"
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
    # Confirm top level keys in the ModelDefinitionList
    required_top_level_keys = ["database", "models", "dependencies"]
    for field_name in config.keys():
        if field_name not in required_top_level_keys:
            raise ValueError(f"Invalid field name {field_name} in config")

    # For each ModelDefinition confirm fields are valid
    models = config["models"]
    model_names = [model["name"] for model in models]
    for model in models:
        if any(
            field_name not in ModelDefinition.model_fields.keys()
            for field_name in model.keys()
        ):
            raise ValueError(f"Invalid field name in ModelDefinition `{model['name']}`")
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

    # For each DependencyDefinition confirm fields are valid (optional so we can sub with empty list)
    dependency_defs = config.get("dependencies", [])
    for dependency in dependency_defs:
        if any(
            field_name not in DependencyDefinition.model_fields.keys()
            for field_name in dependency.keys()
        ):
            raise ValueError(
                f"Invalid field name in DependencyDefinition `{dependency['base']}`"
            )


########################################
# Parse Model Definition               #
########################################


def parse_model_definition(config) -> Tuple[DatabaseConfig, ModelDefinitionList]:
    """Parse the model definition from the config.
    Args:
        config: Dict
    Returns:
        ModelDefinitionList

    """
    models = []
    dependencies = []

    # Parse the DB connection
    db_config_dict = config["database"]
    db_config = DatabaseConfig(
        db_type=db_config_dict["db_type"],
        db_uri_env_var=db_config_dict["db_uri_env_var"],
    )

    # Parse the models
    for model in config["models"]:
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

        models.append(ModelDefinition(name=model["name"], fields=fields))

    # Parse the dependencies (optional, yet to be implemented)
    dependencies = []
    dependency_defs = config.get("dependencies", [])
    for dependency in dependency_defs:
        dependencies.append(DependencyDefinition(**dependency))

    models_def = ModelDefinitionList(models=models, dependencies=dependencies)
    return db_config, models_def
