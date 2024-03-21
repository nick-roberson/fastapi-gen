import argparse
import os

from rich import print

from generate.generate import generate
from generate.models import Config

DEFAULT_INPUT: str = "examples/models.yaml"
DEFAULT_OUTPUT: str = f"{os.getcwd()}/output"


def parse_args():
    """Parse the CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Simple CLI to generate models and services from a yaml config."
    )
    parser.add_argument(
        "--config",
        "-c",
        type=str,
        default=DEFAULT_INPUT,
        help="Path to the input yaml config.",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        type=str,
        default=DEFAULT_OUTPUT,
        help="Path to the output directory.",
    )
    return parser.parse_args()


def generate_files(args: argparse.Namespace):
    """Generate the models and services from the input yaml config."""
    # Simple validation on the input
    if not args.config.endswith(".yaml"):
        raise ValueError("Input must be a yaml file")
    if not os.path.exists(args.config):
        raise ValueError(f"Input file not found at {args.config}")

    # Create the output directory if it doesn't exist
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    print(
        f"""Generating models and services with the following inputs
    Input:  {args.config}
    Output: {args.output_dir}
    """
    )

    # Generate those files in that directory
    result = generate(output_dir=args.output_dir, input_file=args.config)
    print(f"Generated files:")
    print(f"  Models:  {result['models']}")
    print(f"  Service: {result['service']}")
    print(f"  Manager: {result['managers']}")
    print(f"  Mongo:   {result['mongo']}")

    # Display commands for users to go and run the generated files
    print(f"\nRun the following commands to run the service:")
    print(f"  % cd {args.output_dir}")
    print(f"  % poetry run uvicorn service:app --reload --port 8000")


if __name__ == "__main__":
    generate_files(parse_args())
