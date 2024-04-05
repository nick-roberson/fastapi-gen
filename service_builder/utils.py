import os
import subprocess

from rich import print

from service_builder.constants import VERBOSE


def clear_directory(directory: str) -> None:
    """Safely clear a directory.

    Args:
        directory (str): The directory to clear
    """
    try:
        # If the directory exists, clear it
        if os.path.exists(directory):
            run_command(f"rm -rf {directory}", tabs=2)

        # Create the directory
        os.makedirs(directory, exist_ok=True)
    except Exception as e:
        print(f"Error clearing directory: {directory}, {e}")
        raise e


def clear_file(file_path: str) -> None:
    """Safely clear a file.

    Args:
        file_path (str): The file to clear
    """
    try:
        # If the file exists, clear it
        if os.path.exists(file_path):
            run_command(f"rm -f {file_path}", tabs=2)
    except Exception as e:
        print(f"Error clearing file: {file_path}, {e}")
        raise e


def run_command(
    cmd: str, cwd: str = None, tabs: int = 2
) -> subprocess.CompletedProcess:
    """Run a shell command and print the output.

    Args:
        cmd (str): The shell command to run
        cwd (str): The current working directory
        tabs (int): Number of tabs to print before the command
    Returns:
        subprocess.CompletedProcess: The completed process
    """
    try:
        # Create args for command
        args = {
            "shell": True,
            "stdout": subprocess.PIPE,
            "stderr": subprocess.PIPE,
            "text": True,
        }
        if cwd:
            args["cwd"] = cwd

        # Run command and log output
        print(f"{''.join(['\t' for _ in range(tabs)])}> '{cmd}'")
        if VERBOSE:
            completed_process = subprocess.run(cmd, **args)
            print(completed_process.stdout)
            print(completed_process.stderr)
        else:
            completed_process = subprocess.run(cmd, **args)
        return completed_process

    except Exception as e:
        print(f"Error running command: {cmd}, {e}")
        raise e
