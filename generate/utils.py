import subprocess

from rich import print


def run_command(cmd: str, cwd: str = None) -> subprocess.CompletedProcess:
    """Run a shell command and print the output.

    Args:
        cmd (str): The shell command to run
        cwd (str): The current working directory
    Returns:
        subprocess.CompletedProcess: The completed process
    """
    try:
        print(f"Running command '{cmd}'...")
        if cwd:
            completed_process = subprocess.run(cmd, shell=True, check=True, cwd=cwd)
        else:
            completed_process = subprocess.run(cmd, shell=True, check=True)
        return completed_process
    except Exception as e:
        print(f"Error running command: {cmd}, {e}")
        raise e
