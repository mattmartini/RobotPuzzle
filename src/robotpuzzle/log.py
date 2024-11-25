"""Logging Setup"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.0.5"

import json
import logging
import logging.config
import os


class CustomFormatter(logging.Formatter):
    """Custom Formatter does these 2 things:
    1. Overrides 'funcName' with the value of 'func_name_override', if it exists.
    2. Overrides 'filename' with the value of 'file_name_override', if it exists.
    """

    def format(self, record):
        if hasattr(record, "func_name_override"):
            record.funcName = record.func_name_override
        if hasattr(record, "file_name_override"):
            record.filename = record.file_name_override
        return super(CustomFormatter, self).format(record)


def filter_maker(level):
    level = getattr(logging, level)

    def filter(record):
        return record.levelno <= level

    return filter


def get_logger(log_dir="./", log_file="robots2.log"):

    # Create Log file directory if not exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Build Log File Full Path
    logPath = (
        log_file
        if os.path.exists(log_file)
        else os.path.join(log_dir, (str(log_file) + ".log"))
    )

    with open("logging_conf.json", "r") as file:
        logging.config.dictConfig(json.load(file))
    logger = logging.getLogger("RobotLogger")

    return logger
