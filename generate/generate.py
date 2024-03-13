from typing import List
from jinja2 import Environment, FileSystemLoader

from generate.utils import load_config, validate_config, parse_model_definition
from generate.constants import (
    SAMPLE_INPUT,
    MODEL_TEMPLATES,
    OUTPUT_DIR,
    SERVICE_TEMPLATES,
    MANAGER_TEMPLATES,
)
from generate.models import (
    ModelDefinitionList,
    ModelDefinition,
    FieldDefinition,
    DependencyDefinition,
)


def generate_models(models: List[ModelDefinition]) -> str:
    """Use the JINJA Template to generate the models"""
    # Load the template
    env = Environment(loader=FileSystemLoader(MODEL_TEMPLATES))
    model_template = env.get_template("model.jinja")

    # Generate the models
    output = model_template.render(models=models)

    # Write the models to the output directory
    file_name = f"{OUTPUT_DIR}/models/models.py"
    with open(file_name, "w") as f:
        f.write(output)
    return file_name


def generate_services(models: List[ModelDefinition]) -> str:
    """Use the JINJA Template to generate the service"""
    # Load the template
    env = Environment(loader=FileSystemLoader(SERVICE_TEMPLATES))
    service_template = env.get_template("service.jinja")

    # Get list of model names for imports
    model_names = ", ".join([model.name for model in models])
    manager_names = [f"{model.name}Manager" for model in models]

    # Generate the service
    output = service_template.render(
        model_names=model_names, manager_names=manager_names, models=models
    )

    # Write the service to the output directory
    file_name = f"{OUTPUT_DIR}/service.py"
    with open(file_name, "w") as f:
        f.write(output)
    return file_name


def generate_managers(models: List[ModelDefinition]) -> List[str]:
    """Use the JINJA Template to generate the service"""
    manager_file_names = []
    # Load the template
    env = Environment(loader=FileSystemLoader(MANAGER_TEMPLATES))
    service_template = env.get_template("manager.jinja")

    # Get list of model names for imports
    model_names = ", ".join([model.name for model in models])
    for model in models:
        manager_file_name = f"{OUTPUT_DIR}/{model.manager_var_name}.py"

        # Generate the service
        output = service_template.render(model=model, manager_name=model.manager_name)

        # Write the service to the output directory
        with open(manager_file_name, "w") as f:
            f.write(output)
        manager_file_names.append(manager_file_name)
    return manager_file_names


def generate(input: str = SAMPLE_INPUT) -> ModelDefinitionList:
    # Load the config
    config = load_config(input)

    # Validate the config
    validate_config(config)

    # Parse the model definition
    models_def = parse_model_definition(config)
    print(f"Loaded model definition: {models_def}")

    # Generate the models
    model_file = generate_models(models_def.models)
    service_file = generate_services(models_def.models)
    manager_files = generate_managers(models_def.models)

    print(
        f"""Generated models and service:
    Models: {model_file}
    Service: {service_file}
    Manager: {manager_files}
    """
    )
    return models_def
