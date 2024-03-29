import logging
import os
import subprocess


def clear_directory(directory: str) -> None:
    """Clear a directory.

    Args:
        directory (str): The directory to clear
    """
    try:
        # If the directory exists, clear it
        if os.path.exists(directory):
            subprocess.run(f"rm -rf {directory}", shell=True, check=True)

        # Create the directory
        os.makedirs(directory, exist_ok=True)
    except Exception as e:
        logging.info(f"Error clearing directory: {directory}, {e}")
        raise e
