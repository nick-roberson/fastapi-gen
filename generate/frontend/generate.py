import os

from generate.models import Config

OPENAPI_SPEC: str = "openapi.json"


def run_command(cmd: str):
    try:
        print(f"Running command:\n\t> {cmd}")
        os.system(cmd)
    except Exception as e:
        print(f"Error running command: {cmd}")
        raise e


def generate_frontend(output_dir: str):
    """Generates a typescript / react front end from scratch.

    TODO:
        - Import the openapi schema
        - Generate the typescript models
        - Generate the react components
    """
    print("Generating frontend...")

    # (1) navigate to the output directory
    full_path = os.path.abspath(output_dir)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    os.chdir(full_path)

    # (2) Generate the application
    print("Generating the application...")
    service_name = "my-app"
    command = f"npx create-react-app {service_name} --template typescript"
    run_command(command)

    # (3) Generate the front end service code
    print("Generating the models...")
    client_code_dir = f"{full_path}/{service_name}/src/api"
    command = f"openapi-generator generate -i {OPENAPI_SPEC} -g typescript-fetch -o {client_code_dir}"
    run_command(command)
    print("Generated the models!")
