"""Logging Setup"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.0.5"

import json
import logging
import logging.config


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


def get_logger():
    """Creates a Log File and returns Logger object"""

    with open("logging_conf.json", "r") as file:
        logging.config.dictConfig(json.load(file))
    logger = logging.getLogger("RobotLogger")

    """
    logging_conf.json:
    Send messages of severity INFO and WARNING to sys.stdout
    Send messages of severity ERROR and above to sys.stderr
    Send messages of severity DEBUG and above to file app.log
    custom format will put the filename and function name in log

    """
    return logger
