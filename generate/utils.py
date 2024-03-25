import subprocess


def run_command(cmd: str) -> subprocess.CompletedProcess:
    """Run a shell command and print the output.

    Args:
        cmd (str): The shell command to run
    Returns:
        subprocess.CompletedProcess: The completed process
    """
    try:
        print(f"Running command:\n\t> {cmd}")
        completed_process = subprocess.run(cmd, shell=True, check=True)
        return completed_process
    except Exception as e:
        print(f"Error running command: {cmd}, {e}")
        raise e
