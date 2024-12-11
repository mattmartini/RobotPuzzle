"""Buffer for Node"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.4.2"

from rich.panel import Panel
from robotpuzzle import log


class Buffer:
    """Node class: prev and next buffers"""

    def __init__(self):
        """Initialize Buffer"""
        self.input = {"prev": None, "next": None}
        self.output = {"prev": None, "next": None}
        self.logger = log.get_logger()
        self.logger.info("Create buffer")

    def __del__(self):
        """Delete Buffer"""
        self.logger.debug("Delete buffer")

    def __repr__(self):
        """Buffer repr"""
        string = f"Buffer(input:[ {self.input["prev"]}, {self.input["next"]} ], "
        string += f"output:[ {self.output["prev"]}, {self.output["next"]} ])"
        return string

    def __str__(self):
        """Print the Buffer"""

        def vin(ex, fal="_"):
            """Return string based on expression"""
            if ex is None:
                return str(fal)
            return f"{ex}"

        string = " ┌───────────────────┐\n"
        string += f"B│ In:[{vin(self.input["prev"])},{vin(self.input["next"])}] "
        string += f"Out:[{vin(self.output["prev"])},{vin(self.output["next"])}]│\n"
        string += " └───────────────────┘"

        return string

    def buffer_panel(self):
        """Panel of the Buffer"""

        def vin(ex, fal="_"):
            """Return string based on expression"""
            if ex is None:
                return str(fal)
            return f"{ex}"

        string = f" In:[{vin(self.input["prev"])},{vin(self.input["next"])}] "
        string += f"Out:[{vin(self.output["prev"])},{vin(self.output["next"])}]"
        buff_pan = Panel.fit(string)

        return buff_pan

    def get_inputs(self):
        """Input Buffer getter"""
        return [self.input["prev"], self.input["next"]]

    def get_outputs(self):
        """Output Buffer getter"""
        return [self.output["prev"], self.output["next"]]

    def set_inputs(self, pre=None, nex=None):
        """Input Buffer setter"""
        self.input["prev"] = pre
        self.input["next"] = nex
        return [self.input["prev"], self.input["next"]]

    def set_outputs(self, pre=None, nex=None):
        """Output Buffer setter"""
        self.output["prev"] = pre
        self.output["next"] = nex
        return [self.output["prev"], self.output["next"]]
