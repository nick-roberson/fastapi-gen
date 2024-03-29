import datetime
import os
from typing import Dict, List

from service_builder.constants import (DOCKER_TEMPLATES, MANAGER_TEMPLATES,
                                       MODEL_TEMPLATES, MONGO_TEMPLATES,
                                       POETRY_TEMPLATES, PYTHON_DEPENDENCIES,
                                       PYTHON_VERSION, README_TEMPLATES,
                                       SERVICE_TEMPLATES)
from service_builder.generate.utils import populate_template, run_command
from service_builder.models import (DatabaseTypes, DependencyConfig,
                                    ServiceConfig, ServiceVersion)
from service_builder.versions.utils import load_versions, save_version

############################################
# Install Dependencies
############################################


def install_backend_deps(output_dir: str) -> None:
    """Install the backend dependencies using poetry

    Args:
        output_dir (str): Output directory
    """
    # Select the python version
    run_command(f"poetry env use {PYTHON_VERSION}", cwd=output_dir)

    # Install the dependencies
    full_path = os.path.abspath(output_dir)
    run_command(f"poetry install", cwd=full_path)


############################################
# Linting
############################################


def lint_backend(output_dir: str) -> None:
    """Lint the code using black and isort

    Args:
        output_dir (str): Output directory
    """
    run_command(f"poetry run black {output_dir}")
    run_command(f"poetry run isort {output_dir}")


############################################
# Generation
############################################


def generate_models(output_dir: str, config: ServiceConfig) -> str:
    """Use the JINJA Template to generate the models

    Args:
        output_dir (str): Output directory
        config (Config): Configuration object
    Returns:
        str: File name of the generated models
    """
    # Create inputs for the model template
    template_name = "model.jinja"
    output_file = f"{output_dir}/models/models.py"
    context = {"models": config.models}

    # Populate the model file and return the file name
    return populate_template(
        template_dir=MODEL_TEMPLATES,
        template_name=template_name,
        output_path=output_file,
        context=context,
    )


def generate_services(output_dir: str, config: ServiceConfig) -> str:
    """Use the JINJA Template to generate the service

    Args:
        output_dir (str): Output directory
        config (Config): Configuration object
    Returns:
        str: File name of the generated service
    """
    # Get list of model names for imports
    template_name = "service.jinja"
    output_path = f"{output_dir}/service.py"
    model_names = ", ".join([model.name for model in config.models])
    manager_names = [f"{model.name}Manager" for model in config.models]
    context = {
        "models": config.models,
        "model_names": model_names,
        "manager_names": manager_names,
    }

    # Generate the service file and return the file name
    return populate_template(
        template_dir=SERVICE_TEMPLATES,
        template_name=template_name,
        output_path=output_path,
        context=context,
    )


def generate_managers(output_dir: str, config: ServiceConfig) -> List[str]:
    """Use the JINJA Template to generate the service

    Args:
        output_dir (str): Output directory
        config (Config): Configuration object
    Returns:
        List[str]: List of file names of the generated managers
    """
    template_name = "manager.jinja"

    # If the db_type is MONGO, generate the manager
    if config.database.db_type == DatabaseTypes.MONGO.value:
        manager_file_names = []

        for model in config.models:
            # Create inputs for the model template
            output_path = f"{output_dir}/{model.manager_var_name}.py"
            context = {
                "model": model,
                "db_config": config.database,
            }

            # Populate the manager template and append the file name
            output_file = populate_template(
                template_dir=MANAGER_TEMPLATES,
                template_name=template_name,
                output_path=output_path,
                context=context,
            )
            manager_file_names.append(output_file)

        return manager_file_names
    else:
        raise ValueError(
            f"Invalid db_type `{config.database.db_type}`, allowed types are {DatabaseTypes.choices()}"
        )


def generate_database(output_dir: str, config: ServiceConfig) -> str:
    """Use the JINJA Template to generate the database.

    Args:
        output_dir (str): Output directory
        config (Config): Configuration object
    Returns:
        str: File name of the generated database
    """
    # If the db_type is MONGO, generate the db utils
    if config.database.db_type == DatabaseTypes.MONGO.value:
        # Create inputs for the model template
        output_file = f"{output_dir}/mongo.py"
        template_name = "mongo.jinja"

        # Generate the mongo file and return the file name
        return populate_template(
            template_dir=MONGO_TEMPLATES,
            template_name=template_name,
            output_path=output_file,
        )
    else:
        raise ValueError(
            f"Invalid db_type `{config.database.db_type}`, allowed types are {DatabaseTypes.choices()}"
        )


def generate_poetry_toml(output_dir: str, config: ServiceConfig) -> str:
    """Use the JINJA Template to generate the poetry toml file.

    Args:
        output_dir (str): Output directory
        config (Config): Configuration object
    Returns:
        str: File name of the generated poetry toml file
    """
    # Create inputs for the model template
    template_name = "toml.jinja"
    output_path = f"{output_dir}/pyproject.toml"

    dependency_rows = []
    for dep in config.dependencies:
        if dep.version:
            dependency_rows.append(f'{dep.name} = "{dep.version}"')
        else:
            dependency_rows.append(f'{dep.name} = "*"')
    dependency_rows = "\n".join(dependency_rows)

    # TODO: Extend the context with additional fields from config object
    context = {
        "name": "service",
        "version": "0.1.0",
        "description": "My Generated Service",
        "email": "TODO",
        "dependency_rows": dependency_rows,
    }

    # Generate the poetry toml file and return the file name
    return populate_template(
        template_dir=POETRY_TEMPLATES,
        template_name=template_name,
        output_path=output_path,
        context=context,
    )


def generate_readme(output_dir: str) -> str:
    """Use the JINJA Template to generate the README file.

    Args:
        output_dir (str): Output directory
    Returns:
        str: File name of the generated README file
    """
    # Populate the README template
    template_name = "README.jinja"
    output_path = f"{output_dir}/README.md"

    # Generate the README file and return the file name
    return populate_template(
        template_dir=README_TEMPLATES,
        template_name=template_name,
        output_path=output_path,
    )


############################################
# Dockerfile Generation
############################################


def copy_dockerfiles(output_dir: str) -> List[str]:
    """Use the JINJA Template to generate the Dockerfile.

    Args:
        output_dir (str): Output directory
    Returns:
        str: File name of the generated Dockerfile
    """
    # New paths for the dockerfile and docker-compose
    dockerfile_path = f"{DOCKER_TEMPLATES}/Dockerfile"
    compose_path = f"{DOCKER_TEMPLATES}/docker-compose.yml"

    # Copy the dockerfile and docker-compose to the output directory
    os.system(f"cp {dockerfile_path} {output_dir}/Dockerfile")
    os.system(f"cp {compose_path} {output_dir}/docker-compose.yml")

    # Return the file names
    return [dockerfile_path, compose_path]


############################################
# Utility Functions
############################################


def update_versions(
    config: ServiceConfig,
    is_revert: bool = False,
) -> None:
    """Update the versions directory with the new version"""
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


############################################
# Generate Files Main Function
############################################


def generate_files(
    output_dir: str, config: ServiceConfig, is_revert: bool = False
) -> Dict:
    """Generate the models and services from the input yaml config.

    Args:
        output_dir (str): Output directory
        config (Config): Configuration object
        is_revert (bool): Flag to indicate if this is a revert operation
    Returns:
        Dict: Dictionary of the generated files
    """
    # Ensure that the output directory is fully qualified
    output_dir = os.path.abspath(output_dir)
    # Ensure the python code directory is fully qualified
    code_dir = os.path.abspath(f"{output_dir}/src")

    # Generate the models, services, managers, and mongo files
    model_file = generate_models(output_dir=code_dir, config=config)
    service_file = generate_services(output_dir=code_dir, config=config)
    manager_files = generate_managers(output_dir=code_dir, config=config)
    mongo_file = generate_database(output_dir=code_dir, config=config)

    # Generate non code files
    poetry_file = generate_poetry_toml(output_dir=output_dir, config=config)
    readme_file = generate_readme(output_dir=output_dir)
    docker_files = copy_dockerfiles(output_dir=output_dir)

    # Write new version to the versions directory
    update_versions(config=config, is_revert=is_revert)

    # Return the generated files
    return {
        "models": model_file,
        "service": service_file,
        "managers": manager_files,
        "mongo": mongo_file,
        "poetry": poetry_file,
        "readme": readme_file,
        "docker": docker_files,
    }
