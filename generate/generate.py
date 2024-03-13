import os
from typing import Dict, List

from jinja2 import Environment, FileSystemLoader

from generate.constants import (
    MANAGER_TEMPLATES,
    MODEL_TEMPLATES,
    MONGO_TEMPLATES,
    SAMPLE_INPUT,
    SERVICE_TEMPLATES,
)
from generate.models import ModelDefinition
from generate.utils import load_config, parse_model_definition, validate_config


def generate_models(output_dir: str, models: List[ModelDefinition]) -> str:
    """Use the JINJA Template to generate the models"""
    # Load the template
    env = Environment(loader=FileSystemLoader(MODEL_TEMPLATES))
    model_template = env.get_template("model.jinja")

    # Generate the models
    output = model_template.render(models=models)

    # Write the models to the output directory
    file_name = f"{output_dir}/models/models.py"
    if not os.path.exists(file_name):
        os.makedirs(os.path.dirname(file_name), exist_ok=True)

    # Write the models to the output directory
    with open(file_name, "w") as f:
        f.write(output)
    return file_name


def generate_services(output_dir: str, models: List[ModelDefinition]) -> str:
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
    file_name = f"{output_dir}/service.py"
    if not os.path.exists(file_name):
        os.makedirs(os.path.dirname(file_name), exist_ok=True)

    # Write the service to the output directory
    with open(file_name, "w") as f:
        f.write(output)
    return file_name


def generate_managers(output_dir: str, models: List[ModelDefinition]) -> List[str]:
    """Use the JINJA Template to generate the service"""
    manager_file_names = []

    # Load the template
    env = Environment(loader=FileSystemLoader(MANAGER_TEMPLATES))
    service_template = env.get_template("manager.jinja")

    # Get list of model names for imports
    for model in models:
        # Generate the service
        output = service_template.render(model=model, manager_name=model.manager_name)

        # Create the file name
        file_name = f"{output_dir}/{model.manager_var_name}.py"
        if not os.path.exists(file_name):
            os.makedirs(os.path.dirname(file_name), exist_ok=True)

        # Write the service to the output directory
        with open(file_name, "w") as f:
            f.write(output)

        manager_file_names.append(file_name)

    return manager_file_names


def generate_mongo(output_dir: str) -> str:
    """Use the JINJA Template to generate the service"""
    # Load the template
    env = Environment(loader=FileSystemLoader(MONGO_TEMPLATES))
    service_template = env.get_template("mongo.jinja")

    # Generate the service
    output = service_template.render()

    # Write the service to the output directory
    file_name = f"{output_dir}/mongo.py"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(file_name, "w") as f:
        f.write(output)
    return file_name


def clear_output(output_dir: str) -> None:
    """Delete the entire output directory, then recreate it"""
    if os.path.exists(output_dir):
        os.system(f"rm -rf {output_dir}")
    os.makedirs(output_dir)


def generate(output_dir: str, input: str = SAMPLE_INPUT) -> Dict:
    # Load the config and validate
    config = load_config(input)
    validate_config(config)
    models_def = parse_model_definition(config)

    # Clear the output directory
    clear_output(output_dir)

    # Generate the models
    model_file = generate_models(output_dir=output_dir, models=models_def.models)
    service_file = generate_services(output_dir=output_dir, models=models_def.models)
    manager_files = generate_managers(output_dir=output_dir, models=models_def.models)

    # Simple copying of code over
    mongo_file = generate_mongo(output_dir=output_dir)

    return {
        "models": model_file,
        "service": service_file,
        "managers": manager_files,
        "mongo": mongo_file,
    }
