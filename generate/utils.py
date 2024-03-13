import os
import yaml
from typing import Dict
from pydantic.fields import FieldInfo
from generate.models import (
    FieldDefinition,
    ModelDefinition,
    DependencyDefinition,
    ModelDefinitionList,
)

# Pull output the fields from the models
FIELD_DEFINITION_FIELDS: dict[str, FieldInfo] = FieldDefinition.model_fields
MODEL_DEFINITION_FIELDS: dict[str, FieldInfo] = ModelDefinition.model_fields
DEPENDENCY_DEFINITION_FIELDS: dict[str, FieldInfo] = DependencyDefinition.model_fields
MODEL_DEFINITION_LIST_FIELDS: dict[str, FieldInfo] = ModelDefinitionList.model_fields


def load_config(config_path) -> Dict:
    """Simple load config from file path. Error if cannot be found."""
    # Check if the file exists
    if not os.path.exists(config_path):
        raise ValueError(f"Config file not found at {config_path}")
    # Load the config
    with open(config_path, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    # Validate the config
    validate_config(config)
    return config


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


def validate_config(config) -> None:
    """Validate the config to ensure it has the correct fields.

    Args:
        config: Dict
    Returns:
        None
    Raises:
        ValueError: If the config is invalid
    """
    # Confirm top level keys in the ModelDefinitionList
    for field_name in config.keys():
        if field_name not in ModelDefinitionList.model_fields.keys():
            raise ValueError(f"Invalid field name {field_name} in config")

    # For each ModelDefinition confirm fields are valid
    model_names = [model["name"] for model in config["models"]]
    for model in config["models"]:
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

    # For each DependencyDefinition confirm fields are valid
    for dependency in config["dependencies"]:
        if any(
            field_name not in DependencyDefinition.model_fields.keys()
            for field_name in dependency.keys()
        ):
            raise ValueError(
                f"Invalid field name in DependencyDefinition `{dependency['base']}`"
            )


def parse_model_definition(config) -> ModelDefinitionList:
    """Parse the model definition from the config.
    Args:
        config: Dict
    Returns:
        ModelDefinitionList

    """
    models = []
    dependencies = []
    for model in config["models"]:
        fields = []
        for field in model["fields"]:
            fields.append(FieldDefinition(**field))
        models.append(ModelDefinition(name=model["name"], fields=fields))
    for dependency in config["dependencies"]:
        dependencies.append(DependencyDefinition(**dependency))
    return ModelDefinitionList(models=models, dependencies=dependencies)
