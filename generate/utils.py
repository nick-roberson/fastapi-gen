import os
import subprocess

from rich import print

# Constants
VERBOSE: bool = os.environ.get("VERBOSE", False)


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
        print(f"Running command: {cmd}")
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
            print(f"Output: {completed_process.stdout.decode()}")
        return completed_process

    except Exception as e:
        print(f"Error running command: {cmd}, {e}")
        raise e
