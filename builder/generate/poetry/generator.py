import os

from builder.constants import POETRY_TEMPLATES, PYTHON_VERSION
from builder.jinja.templates import populate_template
from builder.models import ServiceConfig
from builder.utils import clear_file, run_command


class PoetryGenerator:
    """
    A class to handle Poetry dependency management and configuration file generation.

    Attributes:
        config (ServiceConfig): Configuration object containing service details.
        output_dir (str): The directory where output files will be saved.
        code_dir (str): The specific directory within output_dir for code-related files.
        poetry_toml (str): Path to the generated poetry TOML file.
        poetry_lock (str): Path to the Poetry lock file.
        requirements_txt (str): Path to the generated requirements.txt file.
        template_path (str): Path to the template file used for generating TOML files.
    """

    CODE_DIR = "backend"  # Directory name for code files
    POETRY_TOML_FILE = "pyproject.toml"
    POETRY_LOCK_FILE = "poetry.lock"
    REQUIREMENTS_TXT_FILE = "requirements.txt"
    TEMPLATE_FILE = "toml.jinja"  # Jinja template file name

    def __init__(self, config: ServiceConfig):
        """
        Initialize the PoetryGenerator with a service configuration.

        Parameters:
            config (ServiceConfig): Configuration object for the service.
        """
        self.config = config
        self.output_dir = config.output_dir
        self.code_dir = os.path.join(self.output_dir, self.CODE_DIR)
        os.makedirs(self.code_dir, exist_ok=True)

        self.poetry_toml = os.path.join(self.code_dir, self.POETRY_TOML_FILE)
        self.poetry_lock = os.path.join(self.code_dir, self.POETRY_LOCK_FILE)
        self.requirements_txt = os.path.join(self.code_dir, self.REQUIREMENTS_TXT_FILE)
        self.template_path = os.path.join(POETRY_TEMPLATES, self.TEMPLATE_FILE)

        if not os.path.exists(self.template_path):
            raise FileNotFoundError(f"Template file {self.template_path} not found")

    def generate_poetry_toml(self) -> str:
        """
        Generate the Poetry TOML file using the specified template.

        Returns:
            str: Path to the generated Poetry TOML file.
        """
        dependency_rows = [
            f'{dep.name} = "{dep.version}"' if dep.version else f'{dep.name} = "*"'
            for dep in self.config.dependencies
        ]
        context = {
            "name": self.config.service_info.name,
            "version": self.config.service_info.version,
            "description": self.config.service_info.description,
            "author": self.config.service_info.author,
            "dependency_rows": "\n".join(dependency_rows),
        }
        return populate_template(
            template_dir=POETRY_TEMPLATES,
            template_name=self.TEMPLATE_FILE,
            output_path=self.poetry_toml,
            context=context,
        )

    def install_dependencies(self) -> None:
        """
        Install the backend dependencies using Poetry.
        """
        run_command(f"poetry env use {PYTHON_VERSION}", cwd=self.code_dir)
        run_command("poetry install", cwd=self.code_dir)
        self.export_requirements()

    def export_requirements(self) -> None:
        """
        Export the requirements.txt file from Poetry.
        """
        run_command(
            f"poetry export -f requirements.txt --output {self.requirements_txt}",
            cwd=self.code_dir,
        )

    def clear_poetry_files(self) -> None:
        """
        Clear all Poetry-related files.
        """
        clear_file(self.poetry_toml)
        clear_file(self.poetry_lock)
        clear_file(self.requirements_txt)
