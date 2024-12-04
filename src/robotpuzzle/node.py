"""Node for circular doubly linked list"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.3.0"

from rich import print
from robotpuzzle import log
from robotpuzzle import buffer


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

    def flush_output_buffers(self):
        """Send data to neighbors, clear outgoing buffers"""
        self.logger.debug(
            "%03d:    %03d <-- %03d", self.id, self.prev.id, self.buffers.output["prev"]
        )
        self.next.buffers.input["next"] = self.buffers.output["prev"]
        self.buffers.output["prev"] = None

        self.logger.debug(
            "%03d:    %03d --> %03d", self.id, self.buffers.output["next"], self.next.id
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
        explosion = f"{self.id:03d}: [red]Boom![/red]"
        print(explosion)
        self.logger.info("%03d: Boom!", self.id)
        return explosion

    def take_action(self, time=""):
        """Action taken this tic or tock"""
        if time == "tic":
            self.logger.debug("%03d: tic", self.id)
            # self.logger.debug(f"{repr(self)}")
            if self.active == 0:
                self.logger.debug("%03d: tic", self.id)
                return
            self.flush_output_buffers()
        elif time == "tock":
            self.logger.debug("%03d: tock", self.id)
            info = self.read_input_buffers()
            if self.active == 0:
                if info == [None, None]:
                    return
                self.activate()
                return
            else:
                # TODO set data and output+buffers
                #  decide on actions: explode or pass data
                if info == [1, 1]:
                    self.turn_inside_out_and_explode()
                self.buffers.output["prev"] = abs(info[0] - 1)
                self.buffers.output["next"] = info[1]
                self.data = self.buffers.output["prev"] & self.buffers.output["next"]
                return info
        else:
            raise ValueError(f"Time is either tic or tock: {time}")


def test():
    """Node test"""
    # testing now done by pytest
    pass


if __name__ == "__main__":
    pass
