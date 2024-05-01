import os
from typing import List

from builder.constants import DOCKER_TEMPLATES
from builder.models import ServiceConfig
from builder.utils import clear_file, run_command


class DockerGenerator:
    """Class to handle Docker file generation."""

    # Class constant for the directory name
    CODE_DIR = "backend"
    # List of Docker related files
    DOCKER_FILES = [
        ".env",
        "Dockerfile",
        "compose.yml",
        ".dockerignore",
        "README.Docker.md",
    ]

    def __init__(self, config: ServiceConfig):
        # Set the config and output directory
        self.config = config
        self.output_dir = config.output_dir

        # Set the code directory
        self.code_dir = os.path.join(self.output_dir, self.CODE_DIR)
        os.makedirs(self.code_dir, exist_ok=True)  # Ensures the directory exists

        # Check all Docker template files exist
        for file in self.DOCKER_FILES:
            src = os.path.join(DOCKER_TEMPLATES, file)
            if not os.path.exists(src):
                raise FileNotFoundError(f"Template file {src} not found")

    def copy_dockerfiles(self) -> List[str]:
        """Copy Docker template files to the output directory."""
        dockerfiles = []
        for file in self.DOCKER_FILES:
            src = os.path.join(DOCKER_TEMPLATES, file)
            dst = os.path.join(self.code_dir, file)
            run_command(f"cp {src} {dst}", cwd=self.code_dir)
            dockerfiles.append(dst)
        return dockerfiles

    def clear_docker_files(self) -> None:
        """Clear Docker-related files."""
        for docker_file in self.DOCKER_FILES:
            clear_file(os.path.join(self.code_dir, docker_file))
