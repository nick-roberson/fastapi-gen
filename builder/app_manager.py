import os
from subprocess import run
from typing import Dict

# Import Generators
from builder.generate.backend.generator import BackendGenerator
from builder.generate.docker.generator import DockerGenerator
from builder.generate.frontend.generator import FrontendGenerator
from builder.generate.linting.manager import LintingManager
from builder.generate.openapi.generator import OpenAPIGenerator
from builder.generate.poetry.generator import PoetryGenerator
from builder.models import ServiceConfig


class ApplicationManager:
    """Class to manage the generation of application components based on configuration."""

    def __init__(self, service_config: ServiceConfig, output_dir: str):
        """
        Initialize the ApplicationManager with service configuration and output directory.

        Args:
            service_config (ServiceConfig): Configuration for the service.
            output_dir (str): Directory where generated files will be placed.
        """
        self.output_dir = output_dir
        self.service_config = service_config
        self.service_name = service_config.service_info.name

        # Backend and frontend code directories
        self.backend_dir = os.path.join(output_dir, "backend")
        self.db_dir = os.path.join(self.backend_dir, "src/db")
        self.frontend_dir = os.path.join(output_dir, self.service_name)

        # Initialize minor generators
        self.docker_generator = DockerGenerator(
            config=service_config, output_dir=output_dir
        )
        self.poetry_generator = PoetryGenerator(
            config=service_config, output_dir=output_dir
        )
        self.openapi_generator = OpenAPIGenerator(
            config=service_config, output_dir=output_dir
        )

        # Initialize major generators
        self.backend_generator = BackendGenerator(
            config=service_config, output_dir=output_dir
        )
        self.frontend_generator = FrontendGenerator(
            config=service_config, output_dir=output_dir
        )

        # Initialize the linting manager
        self.linting_manager = LintingManager(
            config=service_config, output_dir=output_dir
        )

    ####################################################################################################################
    # Commands to run the front and backend services
    ####################################################################################################################

    def run_backend(self):
        """Run the backend service."""
        # Confirm the presence of the backend service
        if not os.path.exists(self.backend_dir):
            raise FileNotFoundError(f"Backend service not found at {self.backend_dir}")

        # Run using poetry
        run(
            ["poetry", "run", "uvicorn", "service:app", "--reload"],
            cwd=self.backend_dir,
        )

    def run_frontend(self):
        """Run the frontend service."""
        # Confirm the presence of the frontend service
        if not os.path.exists(self.frontend_dir):
            raise FileNotFoundError(
                f"Frontend service not found at {self.frontend_dir}"
            )

        # Run using npm
        run(["npm", "start"], cwd=self.frontend_dir)

    ####################################################################################################################
    # Commands to manage DB migrations
    ####################################################################################################################

    def create_migration(self, message: str):
        """Create a new migration for the database."""
        # Confirm the presence of the backend service
        if not os.path.exists(self.db_dir):
            raise FileNotFoundError(f"Backend service not found at {self.db_dir}")

        # Run using alembic using poetry
        commands = [
            "poetry",
            "run",
            "alembic",
            "revision",
            "--autogenerate",
            "-m",
            message,
        ]
        run(commands, cwd=self.db_dir)

    def run_migrations(self):
        """Run the database migrations."""
        # Confirm the presence of the backend service
        if not os.path.exists(self.db_dir):
            raise FileNotFoundError(f"Backend service not found at {self.db_dir}")

        # Run using alembic using poetry
        commands = ["poetry", "run", "alembic", "upgrade", "head"]
        run(commands, cwd=self.db_dir)

    def revert_migration(self, revision: str):
        """Revert the database to a previous revision."""
        # Confirm the presence of the backend service
        if not os.path.exists(self.db_dir):
            raise FileNotFoundError(f"Backend service not found at {self.db_dir}")

        # Run using alembic using poetry
        commands = ["poetry", "run", "alembic", "downgrade", revision]
        run(commands, cwd=self.db_dir)

    def get_migrations(self):
        """Get a list of all migrations."""
        # Confirm the presence of the backend service
        if not os.path.exists(self.db_dir):
            raise FileNotFoundError(f"Backend service not found at {self.db_dir}")

        # Run using alembic using poetry
        print(f"Migrations: {self.service_name}")
        commands = ["poetry", "run", "alembic", "history"]
        run(commands, cwd=self.db_dir)

    ####################################################################################################################
    # Creating new applications from scratch
    ####################################################################################################################

    def generate(
        self,
        backend_only: bool = False,
        frontend_only: bool = False,
        clear: bool = False,
    ) -> Dict:
        """
        Generate the application components as specified in the configuration.

        Args:
            backend_only (bool): If True, only the backend components are generated.
            frontend_only (bool): If True, only the frontend components are generated.
            clear (bool): If True, clear the output directory before generating files.

        Returns:
            Dict: Dictionary containing paths to the generated files and any other relevant data.
        """
        if backend_only:
            return self.generate_backend(clear=clear)

        if frontend_only:
            return self.generate_frontend(clear=clear)

        return self.generate_full_stack(clear=clear)

    def generate_backend(self, clear: bool = False) -> Dict:
        """Generate only the backend components of the application."""
        print("\nGenerating backend services...\n")
        result = self.backend_generator.generate_all(clear=clear)

        print("\nCreating Poetry files and installing deps...\n")
        poetry_toml = self.poetry_generator.generate_poetry_toml()
        self.poetry_generator.install_dependencies()
        result["Poetry Toml"] = poetry_toml

        print("\nCreating Docker files...\n")
        docker_files = self.docker_generator.copy_dockerfiles()
        result["Docker Files"] = docker_files

        print("\nGenerating OpenAPI spec...\n")
        openapi_json_spec = self.openapi_generator.generate_openapi_json()
        result["OpenAPI Spec"] = openapi_json_spec

        print("\nCreating Python Client...\n")
        self.openapi_generator.generate_python_client()
        return result

    def generate_frontend(self, clear: bool = False) -> Dict:
        """Generate only the frontend components of the application."""
        print("\nGenerating frontend services...\n")
        result = self.frontend_generator.generate_all(clear=clear)

        print("\nCreating Typescript Client...\n")
        self.openapi_generator.generate_typescript_client()
        return result

    def generate_full_stack(self, clear: bool = False) -> Dict:
        """Generate both backend and frontend components of the application."""
        # Create and lint backend
        created_files = self.generate_backend(clear=clear)
        self.linting_manager.lint_backend()

        # Create and lint front end
        frontend_files = self.generate_frontend(clear=clear)
        self.linting_manager.lint_frontend()

        # Return the generated files
        return {**created_files, **frontend_files}

    ####################################################################################################################
    # Regenerate the templated components of an existing application
    ####################################################################################################################

    def regenerate(
        self,
        frontend_only: bool = False,
        backend_only: bool = False,
    ) -> Dict:
        """
        Regenerate the templated components of an existing application.

        Args:
            frontend_only (bool): If True, only the frontend components are regenerated.
            backend_only (bool): If True, only the backend components are regenerated.

        Returns:
            Dict: Dictionary containing paths to the generated files and any other relevant data.
        """
        if frontend_only and not backend_only:
            regenerated_files = self.regenerate_frontend()
            self.linting_manager.lint_frontend()
            return regenerated_files

        if backend_only and not frontend_only:
            regenerated_files = self.regenerate_backend()
            self.linting_manager.lint_backend()
            return regenerated_files

        regenerated_files = self.regenerate_full_stack()
        self.linting_manager.lint_all()
        return regenerated_files

    def regenerate_backend(self) -> Dict:
        """Regenerate only the backend components of the application."""
        print("\nRegenerating backend services...\n")
        result = self.backend_generator.generate_templated_components()
        return result

    def regenerate_frontend(self) -> Dict:
        """Regenerate only the frontend components of the application."""
        print("\nRegenerating frontend services...\n")
        result = self.frontend_generator.generate_templated_components()
        return result

    def regenerate_full_stack(self) -> Dict:
        """Regenerate both backend and frontend components of the application."""
        backend_files = self.regenerate_backend()
        frontend_files = self.regenerate_frontend()
        return {**backend_files, **frontend_files}
