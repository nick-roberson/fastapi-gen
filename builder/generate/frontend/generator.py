import os
from string import Template

from jinja2 import Environment, FileSystemLoader
from rich import print

from builder.constants import FRONTEND_TEMPLATES, NODE_DEPENDENCIES
from builder.models import ServiceConfig
from builder.utils import clear_directory, clear_file, run_command


class FrontendGenerator:
    """Class to generate the frontend code for a service."""

    # Create React App command
    CREATE_SERVICE_CMD: Template = Template(
        "npx create-react-app $service_name --template typescript"
    )

    # Install dependencies command
    INSTALL_DEPENDENCIES_CMD: Template = Template("npm install $dependencies")

    # Frontend template files
    INDEX_FILE = "index.tsx"
    HOME_FILE = "components/home.tsx"
    LAYOUT_FILE = "components/layout.tsx"
    NO_PAGE_FILE = "components/no_page.tsx"
    MODEL_PAGE_FILE = "components/model_page.tsx"
    UTILS_FILE = "components/utils.tsx"

    # Frontend auto-generated files to remove
    AUTO_GENERATED_FILES_TO_REMOVE = [
        "App.css",
        "App.test.tsx",
        "App.tsx",
    ]

    def __init__(self, config: ServiceConfig):
        # Set the config and output directory
        self.config = config
        self.output_dir = config.output_dir

        # Set the path for the application
        service_name = self.config.service_info.name
        self.app_dir = os.path.join(self.output_dir, service_name)
        self.src_dir = os.path.join(self.output_dir, service_name, "src")
        self.api_dir = os.path.join(self.output_dir, service_name, "src/api")

        # Application Typescript file
        self.index_tsx = os.path.join(self.src_dir, "index.tsx")

        # Application components
        self.components_dir = os.path.join(self.src_dir, "components")
        self.home_tsx = os.path.join(self.components_dir, "Home.tsx")
        self.layout_tsx = os.path.join(self.components_dir, "Layout.tsx")
        self.no_page_tsx = os.path.join(self.components_dir, "NoPage.tsx")

    def generate_all(self, clear: bool = False):
        """Generate the frontend code"""
        # Clear the frontend code
        if clear:
            print("\t1. Clearing generated frontend code...")
            self.clear_frontend()
        else:
            print("\t1. Skipping clearing of generated frontend code...")

        # Generate the application and install dependencies
        print("\t2. Generating frontend code ...")
        self.generate_application()
        print("\t3. Installing dependencies...")
        self.install_dependencies()

        # Generate the App main page
        print("\t4. Generating App main page...")
        app_main_page = self.generate_templated_components()

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

    def remove_auto_generated_files(self):
        """Remove auto-generated files"""
        for file in self.AUTO_GENERATED_FILES_TO_REMOVE:
            file_path = os.path.join(self.src_dir, file)
            if os.path.exists(file_path):
                clear_file(file_path)

    def generate_templated_components(self):
        """Generate the main page of the application"""
        # Ensure all dirs exist
        if not os.path.exists(self.components_dir):
            os.makedirs(self.components_dir, exist_ok=True)

        # Get env and render the templates
        env = Environment(loader=FileSystemLoader(FRONTEND_TEMPLATES))

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

        # Generate the `utils.tsx` file
        utils_template = env.get_template("components/utils.tsx")
        output = utils_template.render(config=self.config)
        utils_file = os.path.join(self.components_dir, "utils.tsx")
        clear_file(utils_file)
        with open(utils_file, "w") as f:
            f.write(output)

        return {
            "Index.tsx": self.index_tsx,
            "Home": self.home_tsx,
            "Layout": self.layout_tsx,
            "No Page": self.no_page_tsx,
            "Utils": utils_file,
            "Model Pages": model_page_files,
        }
