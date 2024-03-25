import datetime
import os
from typing import Dict, List

from jinja2 import Environment, FileSystemLoader

from generate.backend.constants import (MANAGER_TEMPLATES, MODEL_TEMPLATES,
                                        MONGO_TEMPLATES, POETRY_TEMPLATES,
                                        README_TEMPLATES, SERVICE_TEMPLATES)
from generate.backend.openapi.export_openapi import export_openapi
from generate.backend.parse import load_config, parse_config, validate_config
from generate.backend.versions.utils import load_versions, save_version
from generate.models import (Config, DatabaseConfig, DatabaseTypes,
                             DependencyConfig, ModelConfig, ServiceVersion)
from generate.utils import run_command


def lint_backend(output_dir: str) -> None:
    """Lint the code using black and isort

    Args:
        output_dir (str): Output directory
    """
    run_command(f"poetry run black {output_dir}")
    run_command(f"poetry run isort {output_dir}")


def generate_models(output_dir: str, models: List[ModelConfig]) -> str:
    """Use the JINJA Template to generate the models

    Args:
        output_dir (str): Output directory
        models (List[ModelConfig]): List of model definitions
    Returns:
        str: File name of the generated models
    """
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


def generate_services(output_dir: str, models: List[ModelConfig]) -> str:
    """Use the JINJA Template to generate the service

    Args:
        output_dir (str): Output directory
        models (List[ModelConfig]): List of model definitions
    Returns:
        str: File name of the generated service
    """
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


def generate_managers(
    output_dir: str, db_config: DatabaseConfig, models: List[ModelConfig]
) -> List[str]:
    """Use the JINJA Template to generate the service

    Args:
        output_dir (str): Output directory
        db_config (DatabaseConfig): Database configuration
        models (List[ModelConfig]): List of model definitions
    Returns:
        List[str]: List of file names of the generated managers
    """
    # If the db_type is MONGO, generate the manager
    if db_config.db_type == DatabaseTypes.MONGO.value:
        manager_file_names = []
        env = Environment(loader=FileSystemLoader(MANAGER_TEMPLATES))
        service_template = env.get_template("manager.jinja")

        # Get list of model names for imports
        for model in models:
            # Generate the service
            output = service_template.render(
                model=model, manager_name=model.manager_name
            )

            # Create the file name
            file_name = f"{output_dir}/{model.manager_var_name}.py"
            if not os.path.exists(file_name):
                os.makedirs(os.path.dirname(file_name), exist_ok=True)

            # Write the service to the output directory
            with open(file_name, "w") as f:
                f.write(output)

            manager_file_names.append(file_name)
        return manager_file_names
    else:
        raise ValueError(
            f"Invalid db_type `{db_config.db_type}`, allowed types are {DatabaseTypes.choices()}"
        )


def generate_database(output_dir: str, db_config: DatabaseConfig) -> str:
    """Use the JINJA Template to generate the database.

    Args:
        output_dir (str): Output directory
        db_config (DatabaseConfig): Database configuration
    Returns:
        str: File name of the generated database
    """
    # If the db_type is MONGO, generate the db utils
    if db_config.db_type == DatabaseTypes.MONGO.value:
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
    else:
        raise ValueError(
            f"Invalid db_type `{db_config.db_type}`, allowed types are {DatabaseTypes.choices()}"
        )
    return file_name


def generate_poetry_toml(output_dir: str, dependencies: List[DependencyConfig]) -> str:
    """Use the JINJA Template to generate the poetry toml file.

    Args:
        output_dir (str): Output directory
    Returns:
        str: File name of the generated poetry toml file
    """
    # Load the template
    env = Environment(loader=FileSystemLoader(POETRY_TEMPLATES))
    service_template = env.get_template("toml.jinja")

    # Create a list of dependencies
    dependency_rows = []
    for dep in dependencies:
        if dep.version:
            dependency_rows.append(f'{dep.name} = "{dep.version}"')
        else:
            dependency_rows.append(f'{dep.name} = "*"')
    dependency_rows = "\n".join(dependency_rows)

    # Generate the service
    output = service_template.render(
        name="service",
        version="0.1.0",
        description="My Generated Service",
        email="TODO",
        dependency_rows=dependency_rows,
    )

    # Write the service to the output directory
    file_name = f"{output_dir}/pyproject.toml"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(file_name, "w") as f:
        f.write(output)
    return file_name


def generate_readme(output_dir: str) -> str:
    """Use the JINJA Template to generate the README file.

    Args:
        output_dir (str): Output directory
    Returns:
        str: File name of the generated README file
    """
    # Load the template
    env = Environment(loader=FileSystemLoader(README_TEMPLATES))
    service_template = env.get_template("README.jinja")

    # Generate the service
    output = service_template.render()

    # Write the service to the output directory
    file_name = f"{output_dir}/README.md"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(file_name, "w") as f:
        f.write(output)
    return file_name


def clear_output(output_dir: str) -> None:
    """Delete the entire output directory, then recreate it

    Args:
        output_dir (str): Output directory
    """
    if os.path.exists(output_dir):
        run_command(f"rm -rf {output_dir}")
    os.makedirs(output_dir)


def generate_files(output_dir: str, config: Config, is_revert: bool = False) -> Dict:
    """Generate the models and services from the input yaml config.

    Args:
        output_dir (str): Output directory
        config (Config): Configuration object
        is_revert (bool): Flag to indicate if this is a revert operation
    Returns:
        Dict: Dictionary of the generated files
    """
    # Clear the output directory
    clear_output(output_dir)

    # Generate the models and other code
    model_file = generate_models(output_dir=output_dir, models=config.models)
    service_file = generate_services(output_dir=output_dir, models=config.models)
    manager_files = generate_managers(
        output_dir=output_dir, models=config.models, db_config=config.database
    )
    mongo_file = generate_database(output_dir=output_dir, db_config=config.database)

    # Generate the poetry toml file
    poetry_file = generate_poetry_toml(
        output_dir=output_dir, dependencies=config.dependencies
    )

    # Generate the README file
    readme_file = generate_readme(output_dir=output_dir)

    # Write new version to the versions directory
    # Load previous versions
    if not is_revert:
        new_version = 1
        service_versions = load_versions()
        if service_versions:
            new_version = len(service_versions) + 1

        new_version = ServiceVersion(
            version=new_version,
            name="Service Version",
            created_at=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            db_config=config.database,
            models=config.models,
            dependencies=config.dependencies,
        )
        save_version(new_version)

    # Return the generated files
    return {
        "models": model_file,
        "service": service_file,
        "managers": manager_files,
        "mongo": mongo_file,
        "poetry": poetry_file,
        "readme": readme_file,
    }
