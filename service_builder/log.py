""" Folder that contains all script logging logic """

import logging
import os
from datetime import datetime
from typing import Optional

VERBOSE: bool = os.environ.get("VERBOSE", False)


class CustomFormatter(logging.Formatter):
    """TODO: potentially delete if we are not going to be using this ..."""

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def setup_logging(
    log_level: Optional[str] = "INFO", log_dir: Optional[str] = None
) -> None:
    """Setup logging for the application.

    Args:
        log_level (str): The log level
        log_dir (str): The log directory
    """
    # Set the log level
    log_level = logging.DEBUG if VERBOSE else log_level
    logging.basicConfig(level=log_level)

    # Set the log directory
    log_dir = log_dir or "logs"
    os.makedirs(log_dir, exist_ok=True)

    # Set the log file
    log_file = os.path.join(log_dir, f"{datetime.now().isoformat()}.log")
    file_handler = logging.FileHandler(log_file)
    logging.getLogger().addHandler(file_handler)
    logging.debug(f"Logging to file: {log_file}")
