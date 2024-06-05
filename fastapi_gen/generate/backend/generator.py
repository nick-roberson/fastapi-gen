import os
from string import Template
from typing import Dict, List

from rich import print

from fastapi_gen.constants import (ALEMBIC_TEMPLATES, DOCKER_TEMPLATES,
                                   MODEL_TEMPLATES, README_TEMPLATES,
                                   SERVICE_TEMPLATES)
from fastapi_gen.jinja.templates import populate_template
from fastapi_gen.models import DatabaseTypes, ServiceConfig
from fastapi_gen.utils import clear_directory, clear_file, run_command


class BackendGenerator:
    """Class to generate all the backend code for a service."""

    # Python file name constants
    SERVICE_FILE: str = "service.py"
    MODELS_FILE: str = "models.py"

    # Python code directories
    BACKEND_DIR: str = "backend"
    MODELS_DIR: str = "models"
    DB_DIR: str = "db"
    CLIENT_DIR: str = "client"
    SRC_CODE_DIR: str = "src"
    ALEMBIC_DIR: str = "alembic"

    # Docker files
    DOCKERFILES: List[str] = [
        ".env",
        "Dockerfile",
        "compose.yml",
        ".dockerignore",
        "README.Docker.md",
    ]

    # Alembic files
    ALEMBIC_CP_FILES: List[str] = [
        "alembic/script.py.mako",
        "alembic/README",
        "alembic.ini",
    ]
    ALEMBIC_TEMPLATE_FILES: List[str] = [
        "alembic/env.jinja",
        "models.jinja",
        "manager.jinja",
        "constants.jinja",
    ]

    # Generate python client command
    PYTHON_CLIENT_CMD: Template = Template(
        "openapi-generator generate -i $openapi_spec -g python -o $output_dir"
    )

    def __init__(self, config: ServiceConfig):
        # Set the config and output directory
        self.config = config
        self.output_dir = config.output_dir

        # Top level dir for generated python client code
        self.client_dir = os.path.join(self.output_dir, self.CLIENT_DIR)

        # Top level dir for generated python code
        self.code_dir = os.path.join(self.output_dir, self.BACKEND_DIR)

        # Hold backend/service.py files
        self.service_file = os.path.join(self.code_dir, self.SERVICE_FILE)

        # Hold backend/src/*.py files
        self.src_code_dir = os.path.join(self.code_dir, self.SRC_CODE_DIR)

        # Hold backend/src/db/*.py files
        self.db_dir = os.path.join(self.src_code_dir, self.DB_DIR)
        self.alembic_dir = os.path.join(self.db_dir, self.ALEMBIC_DIR)

        # Hold backend/src/models/*.py files
        self.models_dir = os.path.join(self.src_code_dir, self.MODELS_DIR)
        self.models_file = os.path.join(self.models_dir, self.MODELS_FILE)

        # Hold the docker files
        self.docker_files = [
            os.path.join(self.code_dir, file) for file in self.DOCKERFILES
        ]

        # Ensure that the directories exist
        os.makedirs(self.code_dir, exist_ok=True)
        os.makedirs(self.src_code_dir, exist_ok=True)
        os.makedirs(self.db_dir, exist_ok=True)
        os.makedirs(self.models_dir, exist_ok=True)

    ####################################################################################################################
    # Main Functions for Generating Backend Code
    ####################################################################################################################

    def generate_all(self, clear: bool = True) -> Dict:
        """Generate the backend code for the service.

        Args:
            clear (bool, optional): Whether to clear the output directory. Defaults to True.
        Returns:
            Dict: Dictionary of the generated files
        """
        # Clear the output directory
        if clear:
            print("\t1. Clearing the output directory...")
            self.clear_output()
        else:
            print("\t1. Skipping clearing the output directory...")

        # Generate the models, services, managers, and files
        print("\t2. Generating the backend code...")
        templated_files = self.generate_templated_components()
        self.create_init_files()

        # Return the generated files
        return {
            "Backend Files": {
                **templated_files,
            },
            "Backend Directories": {
                "Service Code": self.code_dir,
                "Python Client Code": self.client_dir,
            },
        }

    def generate_templated_components(self):
        """Generate the templated components for the backend service."""
        # Generate the models, services, and database files
        model_file = self.generate_models()
        service_file = self.generate_services()
        database_files = self.generate_database()
        readme_file = self.generate_readme()
        return {
            "Pydantic Models": model_file,
            "FastAPI Service": service_file,
            "Database": database_files,
            "README.md": readme_file,
        }

    ####################################################################################################################
    # Generate Models, Services, and Database
    ####################################################################################################################

    def generate_database(self):
        """Use the JINJA Template to generate the database file.

        Returns:
            str: File name of the generated database
        """
        db_type = self.config.database.db_type

        # Check valid db_type
        if db_type in DatabaseTypes.choices():
            created_files = self._generate_alembic_db()
            return created_files
        # Otherwise, raise an error
        else:
            raise ValueError(
                f"Invalid db_type '{db_type}', allowed types are {DatabaseTypes.choices()}"
            )

    def _generate_alembic_db(self):
        """Generate the Alembic database files."""
        # First copy over the alembic template files
        alembic_files = []
        for file in self.ALEMBIC_CP_FILES:
            src = os.path.join(ALEMBIC_TEMPLATES, file)
            dst = os.path.join(self.db_dir, file)
            if not os.path.exists(os.path.dirname(dst)):
                os.makedirs(os.path.dirname(dst), exist_ok=True)
            run_command(f"cp {src} {dst}", cwd=self.code_dir)
            alembic_files.append(dst)

        # Create versions dir for alembic
        versions_dir = os.path.join(self.alembic_dir, "versions")
        os.makedirs(versions_dir, exist_ok=True)

        # Handle models.py
        output_path = os.path.join(self.db_dir, "models.py")
        populate_template(
            template_dir=ALEMBIC_TEMPLATES,
            template_name="models.jinja",
            output_path=output_path,
            context={
                "models": self.config.models,
                "schema_name": self.config.service_info.name,
            },
        )

        # Handle *_managers.py
        manager_file_names = []
        for model in self.config.models:
            # Create inputs for the model template
            output_path = os.path.join(self.db_dir, f"{model.manager_var_name}.py")
            context = {
                "model": model,
            }

            # Populate the manager template and append the file name
            output_file = populate_template(
                template_dir=ALEMBIC_TEMPLATES,
                template_name="manager.jinja",
                output_path=output_path,
                context=context,
            )
            manager_file_names.append(output_file)

        # Handle utils.py
        output_path = os.path.join(self.db_dir, "utils.py")
        populate_template(
            template_dir=ALEMBIC_TEMPLATES,
            template_name="utils.jinja",
            output_path=output_path,
            context={"db_models": [f"DB{model.name}" for model in self.config.models]},
        )

        # Handle constants.py
        output_path = os.path.join(self.db_dir, "constants.py")
        populate_template(
            template_dir=ALEMBIC_TEMPLATES,
            template_name="constants.jinja",
            output_path=output_path,
            context={
                "models": self.config.models,
                "db_config": self.config.database,
            },
        )

        # Handle alembic/env.py
        output_path = os.path.join(self.alembic_dir, "env.py")
        populate_template(
            template_dir=ALEMBIC_TEMPLATES,
            template_name="alembic/env.jinja",
            output_path=output_path,
            context={
                "models": self.config.models,
                "db_config": self.config.database,
                "schema_name": self.config.service_info.name,
            },
        )

        # Return all created files
        return alembic_files + manager_file_names + [output_path]

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

    def generate_services(self) -> List[str]:
        """Use the JINJA Template to generate the service

        Returns:
            List[str]: File names of the generated service and routes
        """
        # Get list of model names for imports
        model_names = ", ".join([model.name for model in self.config.models])
        query_model_names = ", ".join(
            [f"{model.name}Query" for model in self.config.models]
        )
        manager_names = [f"{model.name}Manager" for model in self.config.models]
        context = {
            "models": self.config.models,
            "model_names": model_names,
            "query_model_names": query_model_names,
            "manager_names": manager_names,
            "service_name": self.config.service_info.name,
        }

        # Generate the service file and return the file name
        service_file = populate_template(
            template_dir=SERVICE_TEMPLATES,
            template_name="service.jinja",
            output_path=self.service_file,
            context=context,
        )

        # Generate the routes for each model
        route_files = []
        for model in self.config.models:
            context = {
                "models": [model],
                "model_name": model.name,
                "query_model_name": f"{model.name}Query",
                "manager_names": [f"{model.name}Manager"],
            }
            file_name = f"{model.name.lower()}_routes.py"
            output_path = os.path.join(self.code_dir, self.SRC_CODE_DIR, file_name)
            route_file = populate_template(
                template_dir=SERVICE_TEMPLATES,
                template_name="route.jinja",
                output_path=output_path,
                context=context,
            )
            route_files.append(route_file)

        # Return the service file and route files
        return [service_file] + route_files

    ####################################################################################################################
    # Clear Output and Generated Files
    ####################################################################################################################

    def clear_output(self):
        """Clear the output python code directory"""
        # Clear the python code dirs
        clear_directory(self.code_dir)
        clear_directory(self.client_dir)

        # Clear the openapi spec file

        # Clear the docker files
        for docker_file in self.docker_files:
            clear_file(docker_file)

        # Clear models managers and service files
        clear_file(self.models_file)
        clear_file(self.service_file)

    ####################################################################################################################
    # Generate README and Docker Files
    ####################################################################################################################

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

    ####################################################################################################################
    # Create __init__.py Files under each directory
    ####################################################################################################################

    def create_init_files(self):
        """Create __init__.py files under each directory"""
        # Create the __init__.py file for the code directory
        init_file = os.path.join(self.code_dir, "__init__.py")
        if not os.path.exists(init_file):
            run_command(f"touch {init_file}")

        # For each directory in the code dir create an __init__.py file if it does not exist
        for root, directories, files in os.walk(self.code_dir):
            for directory in directories:
                init_file = os.path.join(root, directory, "__init__.py")
                if not os.path.exists(init_file):
                    run_command(f"touch {init_file}")
