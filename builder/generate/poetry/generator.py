import os

from builder.constants import POETRY_TEMPLATES, PYTHON_VERSION
from builder.jinja.templates import populate_template
from builder.models import ServiceConfig
from builder.utils import clear_file, run_command


class PoetryGenerator:
    """Class to handle Poetry dependencies and configuration files."""

    # Class constant for the directory name
    CODE_DIR = "backend"

    # Poetry files
    POETRY_TOML_FILE = "pyproject.toml"
    POETRY_LOCK_FILE = "poetry.lock"
    REQUIREMENTS_TXT_FILE = "requirements.txt"

    # Template file
    TEMPLATE_FILE = "toml.jinja"

    def __init__(self, config: ServiceConfig):
        # Set the config and output directory
        self.config = config
        self.output_dir = config.output_dir

        # Define the code directory
        self.code_dir = os.path.join(self.output_dir, self.CODE_DIR)
        os.makedirs(self.code_dir, exist_ok=True)

        # Define paths for the poetry files
        self.poetry_toml = os.path.join(self.code_dir, self.POETRY_TOML_FILE)
        self.poetry_lock = os.path.join(self.code_dir, self.POETRY_LOCK_FILE)
        self.requirements_txt = os.path.join(self.code_dir, self.REQUIREMENTS_TXT_FILE)

        # Check template exists
        self.template_path = os.path.join(POETRY_TEMPLATES, self.TEMPLATE_FILE)
        if not os.path.exists(self.template_path):
            raise FileNotFoundError(f"Template file {self.template_path} not found")

    def generate_poetry_toml(self) -> str:
        """Generate the poetry toml file using template."""
        dependency_rows = [
            f'{dep.name} = "{dep.version}"' if dep.version else f'{dep.name} = "*"'
            for dep in self.config.dependencies
        ]
        context = {
            "name": self.config.service_info.name,
            "version": self.config.service_info.version,
            "description": self.config.service_info.description,
            "email": self.config.service_info.email,
            "dependency_rows": "\n".join(dependency_rows),
        }
        return populate_template(
            template_dir=POETRY_TEMPLATES,
            template_name=self.TEMPLATE_FILE,
            output_path=self.poetry_toml,
            context=context,
        )

    def install_dependencies(self) -> None:
        """Install the backend dependencies using poetry."""
        run_command(f"poetry env use {PYTHON_VERSION}", cwd=self.code_dir)
        run_command("poetry install", cwd=self.code_dir)
        self.export_requirements()

    def export_requirements(self) -> None:
        """Export requirements.txt from Poetry."""
        run_command(
            f"poetry export -f requirements.txt --output {self.requirements_txt}",
            cwd=self.code_dir,
        )

    def clear_poetry_files(self) -> None:
        """Clear Poetry-related files."""
        clear_file(self.poetry_toml)
        clear_file(self.poetry_lock)
        clear_file(self.requirements_txt)
