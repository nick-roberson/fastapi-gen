import os
from string import Template

from jinja2 import Environment, FileSystemLoader
from rich import print

from builder.constants import (FRONTEND_TEMPLATES, NODE_DEPENDENCIES,
                               OPENAPI_SPEC_FN)
from builder.models import ServiceConfig
from builder.utils import clear_directory, clear_file, run_command


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

    # Frontend template files
    APP_FILE = "App.tsx"
    INDEX_FILE = "index.tsx"
    HOME_FILE = "components/home.tsx"
    LAYOUT_FILE = "components/layout.tsx"
    NO_PAGE_FILE = "components/no_page.tsx"
    MODEL_PAGE_FILE = "components/model_page.tsx"

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
        self.app_tsx = os.path.join(self.src_dir, "App.tsx")
        self.index_tsx = os.path.join(self.src_dir, "index.tsx")

        # Application components
        self.components_dir = os.path.join(self.src_dir, "components")
        self.home_tsx = os.path.join(self.components_dir, "Home.tsx")
        self.layout_tsx = os.path.join(self.components_dir, "Layout.tsx")
        self.no_page_tsx = os.path.join(self.components_dir, "NoPage.tsx")

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
        app_main_page = self.generate_templated_components()

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

    def generate_templated_components(self):
        """Generate the main page of the application"""
        # Ensure all dirs exist
        if not os.path.exists(self.components_dir):
            os.makedirs(self.components_dir, exist_ok=True)

        # Get env and render the templates
        env = Environment(loader=FileSystemLoader(FRONTEND_TEMPLATES))

        # Generate the App.tsx file
        frontend_template = env.get_template(self.APP_FILE)
        output = frontend_template.render(
            service_info=self.config.service_info, models=self.config.models
        )
        clear_file(self.app_tsx)
        with open(self.app_tsx, "w") as f:
            f.write(output)

        # Generate the index.tsx file
        frontend_template = env.get_template(self.INDEX_FILE)
        output = frontend_template.render(config=self.config)
        clear_file(self.index_tsx)
        with open(self.index_tsx, "w") as f:
            f.write(output)

        # Generate the home.tsx file
        frontend_template = env.get_template(self.HOME_FILE)
        output = frontend_template.render(config=self.config)
        clear_file(self.home_tsx)
        with open(self.home_tsx, "w") as f:
            f.write(output)

        # Generate the layout.tsx file
        frontend_template = env.get_template(self.LAYOUT_FILE)
        output = frontend_template.render(config=self.config)
        clear_file(self.layout_tsx)
        with open(self.layout_tsx, "w") as f:
            f.write(output)

        # Generate the nopage.tsx file
        frontend_template = env.get_template(self.NO_PAGE_FILE)
        output = frontend_template.render(config=self.config)
        clear_file(self.no_page_tsx)
        with open(self.no_page_tsx, "w") as f:
            f.write(output)

        # For each model generate a page
        model_page_files = []
        for model in self.config.models:
            frontend_template = env.get_template(self.MODEL_PAGE_FILE)
            output = frontend_template.render(model=model, config=self.config)
            model_file = os.path.join(
                self.components_dir, f"{model.name.lower()}_page.tsx"
            )
            clear_file(model_file)
            with open(model_file, "w") as f:
                f.write(output)
            model_page_files.append(model_file)

        return {
            "App.tsx": self.app_tsx,
            "Index.tsx": self.index_tsx,
            "home.tsx": self.home_tsx,
            "layout.tsx": self.layout_tsx,
            "nopage.tsx": self.no_page_tsx,
            "Model Pages": model_page_files,
        }

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
