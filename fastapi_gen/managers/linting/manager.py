import os
from typing import Dict

from fastapi_gen.models import ServiceConfig
from fastapi_gen.utils import run_command


class LintingManager:
    """Class to handle linting operations for different parts of a service based on its configuration."""

    def __init__(self, config: ServiceConfig):
        """
        Initialize the LintingManager with the service configuration and output directory.
        Args:
            config (ServiceConfig): The configuration for the service.
        """
        # Set the configuration and output directory
        self.config = config
        self.output_dir = config.output_dir

        # Set the frontend and backend directories
        self.frontend_dir = os.path.join(
            self.output_dir, config.service_info.name, "src"
        )
        self.backend_dir = os.path.join(self.output_dir, "backend", "src")

    def lint_code(self, directory: str, tools: Dict):
        """
        Lint the code in the specified directory using given tools.
        Args:
            directory (str): The directory where linting needs to be performed.
            tools (dict): A dictionary where keys are the linting tools and values are the command options.
                          Example: {'prettier': '--write', 'eslint': '--fix'}
        """
        for tool, options in tools.items():
            command = f"{tool} {options} ."
            print(f"Linting directory: {directory} with command `{command}`")
            run_command(cmd=command, cwd=directory, show_output=True)

    def lint_all(self):
        """Lint all parts of the service based on the configuration."""
        self.lint_frontend()
        self.lint_backend()

    def lint_frontend(self):
        """Lint frontend-specific code using tools like Prettier and ESLint."""
        tools = {"npx prettier": "--write", "npx eslint": "--fix"}
        self.lint_code(self.frontend_dir, tools)

    def lint_backend(self):
        """Lint backend-specific code using tools like Black and isort."""
        tools = {"poetry run black": "", "poetry run isort": ""}
        self.lint_code(self.backend_dir, tools)
