import os
from string import Template

from jinja2 import Environment, FileSystemLoader
from rich import print

from service_builder.constants import (FRONTEND_TEMPLATES, NODE_DEPENDENCIES,
                                       OPENAPI_SPEC_FN)
from service_builder.models import ServiceConfig
from service_builder.utils import clear_directory, run_command


class FrontendGenerator:
    """Class to generate the frontend code for a service."""

    # Create React App command
    CREATE_SERVICE_CMD: Template = Template(
        "npx create-react-app $service_name --template typescript"
    )

    # Create Typescript Client command
    CREATE_TYPESCRIPT_CLIENT_CMD: Template = Template(
        "openapi-generator generate -i $openapi_spec -g typescript-fetch -o $output_dir"
    )

    # Install dependencies command
    INSTALL_DEPENDENCIES_CMD: Template = Template("npm install $dependencies")

    def __init__(self, output_dir: str, config: ServiceConfig):
        # Set the config and output directory
        self.config = config
        self.output_dir = output_dir

        # Set the path for the application
        service_name = self.config.service_info.name
        self.app_dir = os.path.join(self.output_dir, service_name)
        self.src_dir = os.path.join(self.output_dir, service_name, "src")
        self.api_dir = os.path.join(self.output_dir, service_name, "src/api")

        # OpenAPI Spec file
        self.openapi_spec_fp = os.path.join(self.output_dir, "src", OPENAPI_SPEC_FN)

        # Application Typescript file
        self.app_tsx = os.path.join(self.output_dir, service_name, "src/App.tsx")

    def generate_all(self):
        """Generate the frontend code"""
        print("\t1. Clearing generated frontend code...")
        self.clear_frontend()

        # Generate the application and install dependencies
        print("\t2. Generating frontend code ...")
        self.generate_application()
        print("\t3. Installing dependencies...")
        self.install_dependencies()

        # Generate the App main page
        print("\t4. Generating App main page...")
        app_main_page = self.generate_app_main_page()

        # Generate the typescript client
        print("\t5. Generating Typescript client...")
        self.generate_typescript_client()

        # Lint the code
        print("\t6. Linting frontend code...")
        self.lint_frontend()

        return {
            "Frontend Files": {
                "Main Page": app_main_page,
            },
            "Frontend Directories": {
                "Application Directory": self.app_dir,
                "Source Code": self.src_dir,
                "API Client Code": self.api_dir,
            },
        }

    def clear_frontend(self):
        """Clear the frontend code"""
        # Clear the frontend code directory
        clear_directory(self.app_dir)

    def generate_application(self):
        """Generates a typescript / react front end from scratch."""
        command = self.CREATE_SERVICE_CMD.substitute(
            service_name=self.config.service_info.name
        )
        run_command(cmd=command, cwd=self.output_dir)

    def install_dependencies(self):
        """Install node dependencies using npm"""
        dependencies = " ".join(NODE_DEPENDENCIES)
        command = self.INSTALL_DEPENDENCIES_CMD.substitute(dependencies=dependencies)
        run_command(cmd=command, cwd=self.app_dir)

    def lint_frontend(self):
        """Lint the code using prettier"""
        run_command("npx prettier --write .", cwd=self.src_dir)
        run_command("npx eslint --fix .", cwd=self.src_dir)

    def generate_app_main_page(self):
        """Generate the main page of the application"""
        # Load the template
        env = Environment(loader=FileSystemLoader(FRONTEND_TEMPLATES))
        frontend_template = env.get_template("App.tsx")

        # Generate the models
        output = frontend_template.render(models=self.config.models)

        # Write the models to the output directory
        service_name = self.config.service_info.name
        file_name = f"{self.output_dir}/{service_name}/src/App.tsx"
        if not os.path.exists(file_name):
            os.makedirs(os.path.dirname(file_name), exist_ok=True)

        # Write the models to the output directory
        with open(file_name, "w") as f:
            f.write(output)

        return file_name

    def generate_typescript_client(self):
        """Generate the frontend service client code"""
        # Clear the client code directory
        clear_directory(self.api_dir)

        # Create the client code directory
        if not os.path.exists(self.api_dir):
            os.makedirs(self.api_dir, exist_ok=True)

        # Generate the client code
        command = self.CREATE_TYPESCRIPT_CLIENT_CMD.substitute(
            openapi_spec=self.openapi_spec_fp, output_dir=self.api_dir
        )
        run_command(cmd=command, cwd=self.output_dir)
