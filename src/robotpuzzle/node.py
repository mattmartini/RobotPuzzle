"""Node for circular doubly linked list"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.4.0"

from rich.panel import Panel
from robotpuzzle import log
from robotpuzzle import buffer
from robotpuzzle.console import console


class Node:
    """Node class: Robot instance"""

    count = 0

    @classmethod
    def inc_count(cls):
        """Increment the Class count"""
        cls.count += 1

    def __init__(self, data=None):
        """Initalize Node"""
        self.id = Node.count
        Node.inc_count()
        self._active = False
        self.data = data
        self.prev = self
        self.next = self
        self.buffers = buffer.Buffer()
        self.logger = log.get_logger()

        self.logger.info("Create node %03d", self.id)

    def __del__(self):
        """Delete Node"""
        self.logger.debug("Delete Node %03d", self.id)

    @property
    def active(self):
        """Node Property: Active"""
        return self._active

    @active.setter
    def active(self, active):
        self._active = active

    def activate(self):
        """Activate Node"""
        self.active = True
        self.logger.info("%03d: Activated", self.id)

    def deactivate(self):
        """Deactivate Node"""
        self.active = False
        self.logger.info("%03d: Deactivated", self.id)

    def __repr__(self):
        """Node repr"""
        string = f"Node({self.id:03d}, {self.active}, "
        string += f"{self.data}, {self.prev.id:03d}, {self.next.id:03d})"
        return string

    def __str__(self):
        """Print the Node"""

        def vtf(ex, fal="-", tru="+"):
            """Return string based on expression"""
            if ex == 0:
                return str(fal)
            return str(tru)

        def vin(ex, fal="_"):
            """Return string based on expression"""
            if ex is None:
                return str(fal)
            return f"{ex}"

        string = "╭─────────────────╮\n"
        string += f"│{self.prev.id:03d}  "
        string += f"{vtf(self.active)} {self.id:03d} {vtf(self.active)}  "
        string += f"{self.next.id:03d}│\n"
        string += f"│{vin(self.buffers.output["prev"])}<--"
        string += f" {vin(self.buffers.input["prev"])}  "
        string += f"{vin(self.data)}"
        string += f"  {vin(self.buffers.input["next"])} "
        string += f"-->{vin(self.buffers.output["next"])}│\n"
        string += "╰─────────────────╯"

        return string

    def node_panel(self):
        """Panel of the Node"""

        def vtf(ex, fal="-", tru="+"):
            """Return string based on true/false of expression"""
            if ex == 0:
                return str(fal)
            return str(tru)

        def vin(ex, fal="_"):
            """Return string based on expression is None"""
            if ex is None:
                return str(fal)
            return f"{ex}"

        def vbk(ex, fal="_"):
            """Return color bkg for non None"""
            if ex is None:
                return str(fal)
            return f"[orange1 on grey35]{ex}[/orange1 on grey35]"

        string = f"[tan]{self.prev.id:03d}[/tan]  "
        string += f"{vtf(self.active)} "
        string += f"[bright_white]{self.id:03d}[/bright_white]"
        string += f" {vtf(self.active)}  "
        string += f"[tan]{self.next.id:03d}[/tan]\n"
        string += f"{vbk(self.buffers.output["prev"])}[steel_blue3]<--[/steel_blue3]"
        string += f" {vbk(self.buffers.input["prev"])}  "
        string += f"[misty_rose1]{vin(self.data)}[/misty_rose1]"
        string += f"  {vbk(self.buffers.input["next"])} "
        string += f"[steel_blue3]-->[/steel_blue3]{vbk(self.buffers.output["next"])}"

        if self.active is True:
            nod_pan = Panel.fit(string, style="active_node")
        elif self.active is False:
            nod_pan = Panel.fit(string, style="inactive_node")

        return nod_pan

    def flush_output_buffers(self):
        """Send data to neighbors, clear outgoing buffers"""
        # FIXME want to clear inputs in a way that makes them visible
        # self.buffers.input["prev"] = None
        # self.buffers.input["next"] = None
        self.logger.debug(
            "%03d:    %03d <-- %s", self.id, self.prev.id, self.buffers.output["prev"]
        )
        self.prev.buffers.input["next"] = self.buffers.output["prev"]
        self.buffers.output["prev"] = None

        self.logger.debug(
            "%03d:    %s --> %03d", self.id, self.buffers.output["next"], self.next.id
        )
        self.next.buffers.input["prev"] = self.buffers.output["next"]
        self.buffers.output["next"] = None

    def read_input_buffers(self):
        """Read and clear input buffers"""
        cur_buffers = [self.buffers.input["prev"], self.buffers.input["next"]]
        self.buffers.input["prev"] = None
        self.buffers.input["next"] = None
        self.logger.debug("%03d: input buffers %s", self.id, cur_buffers)
        return cur_buffers

    def turn_inside_out_and_explode(self):
        """Explode"""
        explosion = f"{self.id:03d}: Boom!"
        console.print(explosion, style="explosion")
        self.logger.info("%03d: Boom!", self.id)
        return explosion

    def time_tic(self):
        """Action taken on clock tic"""
        self.logger.debug("%03d: tic", self.id)
        if self.active is False:
            self.logger.debug("%03d: tic - noop", self.id)
            return
        self.flush_output_buffers()

    def time_tock(self):
        """Action taken on clock tock"""
        self.logger.debug("%03d: tock", self.id)
        info = self.read_input_buffers()
        if self.active is False:
            if info == [None, None]:
                self.logger.debug("%03d: tock - noop", self.id)
                return
            self.activate()
            if info[0] == 0:
                self.data = 1
                self.buffers.output["next"] = 0
            if info[0] == 1:
                self.data = 0
                self.buffers.output["next"] = 1
            if info[1] == 0:
                self.data = 1
                self.buffers.output["prev"] = 0
            if info[1] == 1:
                self.data = 0
                self.buffers.output["prev"] = 1
            # if info[0] is not None:
            #     self.buffers.output["next"] = 1
            # if info[1] is not None:
            #     self.buffers.output["prev"] = 1
            return
        else:
            # TODO set data and output+buffers
            #  decide on actions: explode or pass data
            if info[0] == 0:
                self.buffers.output["next"] = self.data
                self.data = 0
            if info[0] == 1:
                self.buffers.output["next"] = self.data
                self.data = 1
            if info[1] == 0:
                self.buffers.output["prev"] = self.data
                self.data = 0
            if info[1] == 1:
                self.buffers.output["prev"] = self.data
                self.data = 1

            if info == [1, 1]:
                self.turn_inside_out_and_explode()
                self.data = "X"
            return info

    def advance_clock(self, time=""):
        """Action taken this tic or tock"""
        if time == "tic":
            self.time_tic()
        elif time == "tock":
            self.time_tock()
        else:
            raise ValueError(f"Time is either tic or tock: {time}")


def test():
    """Node test"""
    # testing now done by pytest
    pass


if __name__ == "__main__":
    pass
