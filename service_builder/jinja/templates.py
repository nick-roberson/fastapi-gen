import logging
import os
import subprocess

from jinja2 import Environment, FileSystemLoader, Template

# Constants
VERBOSE: bool = os.environ.get("VERBOSE", False)


def load_template(template_path: str, template_name: str) -> Template:
    """Load a template file.

    Args:
        template_path (str): The path to the template file
        template_name (str): The name of the template file
    Returns:
        str: The template content
    """
    try:
        # Ensure that the template path is fully qualified and exists
        template_path = os.path.abspath(template_path)
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template path not found: {template_path}")

        # Load the template
        env = Environment(loader=FileSystemLoader(template_path))
        return env.get_template(template_name)
    except Exception as e:
        logging.info(f"Error loading template: {template_path}, {e}")
        raise e


def write_template(template: Template, output_path: str, context: dict) -> None:
    """Write a template to a file.

    Args:
        template (Template): The template content
        output_path (str): The output file path
        context (dict): The context for the template
    """
    try:
        # Render the template
        context = context or {}
        rendered_template = template.render(**context)

        # Write the rendered template to the output path
        with open(output_path, "w") as f:
            f.write(rendered_template)
    except Exception as e:
        logging.info(f"Error writing template: {output_path}, {e}")
        raise e


def populate_template(
    template_dir: str, template_name: str, output_path: str, context: dict = None
) -> str:
    """Populate a template file.

    Args:
        template_dir (str): The path to the template file directory
        template_name (str): The name of the template file
        output_path (str): The output file path
        context (dict): The context for the template
    """
    try:
        # Load the template
        template = load_template(template_dir, template_name)

        # Ensure the output directory exists
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        # Write the template
        write_template(template, output_path, context)
        return output_path

    except Exception as e:
        logging.info(f"Error populating template: {output_path}, {e}")
        raise e


def run_command(cmd: str, cwd: str = None) -> subprocess.CompletedProcess:
    """Run a shell command and print the output.

    Args:
        cmd (str): The shell command to run
        cwd (str): The current working directory
    Returns:
        subprocess.CompletedProcess: The completed process
    """
    try:
        # Print and run the command
        if VERBOSE:
            logging.info(f"Running command: {cmd}")

        # Run the command
        if cwd:
            completed_process = subprocess.run(
                cmd, shell=True, check=True, cwd=cwd, capture_output=True
            )
        else:
            completed_process = subprocess.run(
                cmd, shell=True, check=True, capture_output=True
            )

        # Show output conditionally
        if VERBOSE:
            logging.info(f"Output: {completed_process.stdout.decode()}")
        return completed_process

    except Exception as e:
        logging.info(f"Error running command: {cmd}, {e}")
        raise e
