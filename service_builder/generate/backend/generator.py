import os
from string import Template
from typing import Dict, List

from rich import print

from service_builder.constants import (DOCKER_TEMPLATES, MANAGER_TEMPLATES,
                                       MODEL_TEMPLATES, MONGO_TEMPLATES,
                                       OPENAPI_SPEC_FN, POETRY_TEMPLATES,
                                       PYTHON_VERSION, README_TEMPLATES,
                                       SERVICE_TEMPLATES)
from service_builder.jinja.templates import populate_template
from service_builder.models import DatabaseTypes, ServiceConfig
from service_builder.openapi.export import export_openapi
from service_builder.utils import clear_directory, clear_file, run_command


class BackendGenerator:
    """Class to generate all the backend code for a service along with
    install the dependencies and lint the code.
    """

    # Python file name constants
    SERVICE_FILE: str = "service.py"
    MODELS_FILE: str = "models.py"

    # Poetry file constants
    POETRY_TOML: str = "pyproject.toml"
    POETRY_LOCK: str = "poetry.lock"
    REQUIREMENTS_TXT: str = "requirements.txt"

    # Python code directories
    SRC_DIR: str = "src"
    MODELS_DIR: str = "models"
    MANAGERS_DIR: str = "managers"
    CLIENT_DIR: str = "client"

    # Docker files
    DOCKERFILES: List[str] = [
        "Dockerfile",
        "compose.yml",
        ".dockerignore",
        "README.Docker.md",
    ]

    # Generate python client command
    PYTHON_CLIENT_CMD: Template = Template(
        "openapi-generator generate -i $openapi_spec -g python -o $output_dir"
    )

    def __init__(self, config: ServiceConfig, output_dir: str):
        # Set the config and output directory
        self.config = config
        self.output_dir = output_dir

        # Generated python service and client code
        self.code_dir = os.path.join(self.output_dir, self.SRC_DIR)
        self.client_dir = os.path.join(self.output_dir, self.CLIENT_DIR)

        # Set constant python file names
        self.service_file = os.path.join(self.code_dir, self.SERVICE_FILE)
        self.models_file = os.path.join(
            self.code_dir, self.MODELS_DIR, self.MODELS_FILE
        )

        # Set dependency files
        self.poetry_toml = os.path.join(self.code_dir, self.POETRY_TOML)
        self.poetry_lock = os.path.join(self.code_dir, self.POETRY_LOCK)
        self.requirements_txt = os.path.join(self.code_dir, self.REQUIREMENTS_TXT)

        # Set docker files
        self.docker_files = [
            os.path.join(self.code_dir, file) for file in self.DOCKERFILES
        ]

    def generate_all(self) -> Dict:
        """Generate the backend code for the service.

        Returns:
            Dict: Dictionary of the generated files
        """
        # Clear the output directory
        print("\t1. Clearing the output directory...")
        self.clear_output()

        # Generate the models, services, managers, and mongo files
        print("\t2. Generating the backend code...")
        model_file = self.generate_models()
        service_file = self.generate_services()
        manager_files = self.generate_managers()
        mongo_file = self.generate_database()

        # Generate non code files
        print("\t3. Generating the non-code files (poetry and readme)...")
        poetry_file = self.generate_poetry_toml()
        readme_file = self.generate_readme()

        # Generate the python client code
        print("\t4. Exporting OpenAPI JSON file...")
        self.generate_openapi_file()
        print("\t5. Generating the python client code...")
        self.generate_python_client()

        # Then install the backend dependencies and lint the code
        print("\t6. Installing the backend dependencies...")
        self.install_backend_deps()
        print("\t7. Linting the backend code...")
        self.lint_backend()

        # Return the generated files
        return {
            "Backend Files": {
                "Pydantic Models": [model_file],
                "FastAPI Service": [service_file],
                "Model Managers": manager_files,
                "MongoDB": [mongo_file],
                "README.md": [readme_file],
                "Poetry": [poetry_file],
            },
            "Backend Directories": {
                "Service Code": self.code_dir,
                "Python Client Code": self.client_dir,
            },
        }

    def clear_output(self):
        """Clear the output python code directory"""
        # Clear the python code dirs
        clear_directory(self.code_dir)
        clear_directory(self.client_dir)

        # Clear the poetry files
        clear_file(self.poetry_toml)
        clear_file(self.poetry_lock)
        clear_file(self.requirements_txt)

        # Clear the openapi spec file

        # Clear the docker files
        for docker_file in self.docker_files:
            clear_file(docker_file)

        # Clear models managers and service files
        clear_file(self.models_file)
        clear_file(self.service_file)

    def generate_readme(self):
        """Use the JINJA Template to generate the README file.

        Returns:
            str: File name of the generated README file
        """
        # Populate the README template
        template_name = "README.jinja"
        output_path = f"{self.code_dir}/README.md"

        # Generate the README file and return the file name
        return populate_template(
            template_dir=README_TEMPLATES,
            template_name=template_name,
            output_path=output_path,
        )

    def install_backend_deps(self) -> None:
        """Install the backend dependencies using poetry"""
        # Select the python version and install
        run_command(f"poetry env use {PYTHON_VERSION}", cwd=self.code_dir)
        run_command("poetry install", cwd=self.code_dir)

        # Check that all files are created
        toml_file = os.path.join(self.code_dir, "pyproject.toml")
        lock_file = os.path.join(self.code_dir, "poetry.lock")
        if not os.path.exists(toml_file) or not os.path.exists(lock_file):
            raise ValueError(f"Poetry files not found in {self.code_dir}")

        # Generate the requirements file
        req_file = "requirements.txt"
        run_command(
            f"poetry export -f {req_file} --output {req_file}", cwd=self.code_dir
        )

    def copy_dockerfiles(self):
        """Use the JINJA Template to generate the Dockerfile.

        Returns:
            str: File name of the generated Dockerfile
        """
        # Copy all files into the output directory
        dockerfiles = []
        for file in self.DOCKERFILES:
            src = os.path.join(DOCKER_TEMPLATES, file)
            dst = os.path.join(self.code_dir, file)
            run_command(f"cp {src} {dst}", cwd=self.code_dir)
            dockerfiles.append(dst)

        # Return the file names
        return dockerfiles

    def generate_openapi_file(self):
        return export_openapi(code_dir=self.code_dir)

    def generate_poetry_toml(self) -> str:
        """Use the JINJA Template to generate the poetry toml file.

        Returns:
            str: File name of the generated poetry toml file
        """
        # Create the dependency rows
        dependency_rows = []
        for dep in self.config.dependencies:
            if dep.version:
                dependency_rows.append(f'{dep.name} = "{dep.version}"')
            else:
                dependency_rows.append(f'{dep.name} = "*"')
        dependency_rows = "\n".join(dependency_rows)

        # Create the context for the template
        context = {
            "name": self.config.service_info.name,
            "version": self.config.service_info.version,
            "description": self.config.service_info.description,
            "email": "<enter your email>",
            "dependency_rows": dependency_rows,
        }

        # Generate the poetry toml file and return the file name
        return populate_template(
            template_dir=POETRY_TEMPLATES,
            template_name="toml.jinja",
            output_path=self.poetry_toml,
            context=context,
        )

    def generate_database(self):
        """Use the JINJA Template to generate the database file.

        Returns:
            str: File name of the generated database
        """
        # If the db_type is MONGO, generate the db utils
        if self.config.database.db_type == DatabaseTypes.MONGO.value:
            output_file = f"{self.code_dir}/mongo.py"
            return populate_template(
                template_dir=MONGO_TEMPLATES,
                template_name="mongo.jinja",
                output_path=output_file,
            )
        else:
            raise ValueError(
                f"Invalid db_type '{self.config.database.db_type}', allowed types are {DatabaseTypes.choices()}"
            )

    def generate_managers(self) -> List[str]:
        """Use the JINJA Template to generate the service managers.
        Returns:
            List[str]: List of file names of the generated managers
        """
        # If the db_type is MONGO, generate the manager
        if self.config.database.db_type == DatabaseTypes.MONGO.value:
            manager_file_names = []

            for model in self.config.models:
                # Create inputs for the model template
                output_path = f"{self.code_dir}/{model.manager_var_name}.py"
                context = {
                    "model": model,
                    "db_config": self.config.database,
                }

                # Populate the manager template and append the file name
                output_file = populate_template(
                    template_dir=MANAGER_TEMPLATES,
                    template_name="manager.jinja",
                    output_path=output_path,
                    context=context,
                )
                manager_file_names.append(output_file)

            return manager_file_names
        else:
            raise ValueError(
                f"Invalid db_type '{self.config.database.db_type}', allowed types are {DatabaseTypes.choices()}"
            )

    def lint_backend(self) -> None:
        """Lint the code using black and isort"""
        run_command(f"poetry run black {self.code_dir}")
        run_command(f"poetry run isort {self.code_dir}")

    def generate_models(self) -> str:
        """Use the JINJA Template to generate the models

        Returns:
            str: File name of the generated models
        """
        # Create inputs for the model template

        context = {"models": self.config.models}

        # Populate the model file and return the file name
        return populate_template(
            template_dir=MODEL_TEMPLATES,
            template_name="model.jinja",
            output_path=self.models_file,
            context=context,
        )

    def generate_services(self) -> str:
        """Use the JINJA Template to generate the service

        Returns:
            str: File name of the generated service
        """
        # Get list of model names for imports
        model_names = ", ".join([model.name for model in self.config.models])
        manager_names = [f"{model.name}Manager" for model in self.config.models]
        context = {
            "models": self.config.models,
            "model_names": model_names,
            "manager_names": manager_names,
        }

        # Generate the service file and return the file name
        return populate_template(
            template_dir=SERVICE_TEMPLATES,
            template_name="service.jinja",
            output_path=self.service_file,
            context=context,
        )

    def generate_python_client(self):
        """Generate the python client code"""
        # Create the client code directory
        if not os.path.exists(self.client_dir):
            os.makedirs(self.client_dir, exist_ok=True)

        # Generate the client code
        command = self.PYTHON_CLIENT_CMD.substitute(
            openapi_spec=OPENAPI_SPEC_FN, output_dir=self.client_dir
        )
        run_command(cmd=command, cwd=self.code_dir)
