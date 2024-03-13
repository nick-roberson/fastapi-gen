import argparse
import os

from rich import print

from generate.generate import generate
from generate.models import ModelDefinitionList

DEFAULT_INPUT: str = "examples/models.yaml"
DEFAULT_OUTPUT: str = f"{os.getcwd()}/output"


def parse_args():
    """Parse the CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Simple CLI to generate models and services from a yaml config."
    )
    parser.add_argument(
        "--input",
        type=str,
        default=DEFAULT_INPUT,
        help="Path to the input yaml config.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=DEFAULT_OUTPUT,
        help="Path to the output directory.",
    )
    return parser.parse_args()


def generate_files(args: argparse.Namespace):
    """Generate the models and services from the input yaml config."""
    # Simple validation on the input
    if not args.input.endswith(".yaml"):
        raise ValueError("Input must be a yaml file")
    if not os.path.exists(args.input):
        raise ValueError(f"Input file not found at {args.input}")

    # Create the output directory if it doesn't exist
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    print(
        f"""Generating models and services with the following inputs
    Input:  {args.input}
    Output: {args.output}
    """
    )

    # Generate those files in that directory
    result = generate(output_dir=args.output, input=args.input)
    print(f"Generated files:")
    print(f"  Models:  {result['models']}")
    print(f"  Service: {result['service']}")
    print(f"  Manager: {result['managers']}")
    print(f"  Mongo:   {result['mongo']}")

    # Display commands for users to go and run the generated files
    print(f"\nRun the following commands to run the service:")
    print(f"  % cd {args.output}")
    print(f"  % poetry run uvicorn service:app --reload --port 8000")


if __name__ == "__main__":
    generate_files(parse_args())
