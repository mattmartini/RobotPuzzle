"""Node for circular doubly linked list"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.2.2"

from rich import print

# from rich import pretty
from robotpuzzle import log


class Node:
    """Node class: Robot instance"""

    count = 0

    def __init__(self, data=None):
        """Initalize Node"""
        self.id = Node.count
        Node.count += 1
        self.active = 0
        self.data = data
        self.prev = self
        self.next = self
        self.in_buffer_p = None
        self.in_buffer_n = None
        self.out_buffer_p = None
        self.out_buffer_n = None
        self.logger = log.get_logger()
        self.logger.info("Create node %03d", self.id)

    def __repr__(self):
        """Node repr"""
        string = f"Node({self.id:03d}, {self.active}, "
        string += f"{self.data}, {self.prev.id:03d}, {self.next.id:03d})"
        return string

    def __str__(self):
        """Print the Node"""
        string = "╭────────────────╮\n"
        string += f"│{self.prev.id:03d}  {('-', '+')[self.active]} "
        string += f"{self.id:03d} {('-', '+')[self.active]} {self.next.id:03d}│\n"

        string += f"│{(self.out_buffer_p, '_')[self.out_buffer_p is None]}<--"
        string += f"  {(self.in_buffer_p, '_')[self.in_buffer_p is None]} "
        string += f"{(self.data, '_')[self.data is None]} "
        string += f"{(self.in_buffer_n, '_')[self.in_buffer_n is None]} "
        string += f"-->{(self.out_buffer_n, '_')[self.out_buffer_n is None]}│\n"

        string += "╰────────────────╯"
        # string += "\nHello from [bold magenta]robotpuzzle![/bold magenta]"

        return string

    def flush_output_buffers(self):
        """Send data to neighbors, clear outgoing buffers"""
        self.logger.debug(
            "%03d:    %03d <-- %03d", self.id, self.prev.id, self.out_buffer_p
        )
        self.prev.in_buffer_n = self.out_buffer_p
        self.out_buffer_p = None

        self.logger.debug(
            "%03d:    %03d --> %03d", self.id, self.out_buffer_n, self.next.id
        )
        self.next.in_buffer_p = self.out_buffer_n
        self.out_buffer_n = None

    def read_input_buffers(self):
        """Read and clear input buffers"""
        cur_buffers = [self.in_buffer_p, self.in_buffer_n]
        self.in_buffer_p = None
        self.in_buffer_n = None
        self.logger.debug("%03d: input buffers %s", self.id, cur_buffers)
        return cur_buffers

    def activate(self):
        """Activate Node"""
        self.active = 1
        self.logger.info("%03d: Activated", self.id)

    def deactivate(self):
        """Deactivate Node"""
        self.active = 0
        self.logger.info("%03d: Deactivated", self.id)

    def turn_inside_out_and_explode(self):
        """Explode"""
        explosion = f"{self.id:03d}: [red]Boom![/red]"
        print(explosion)
        self.logger.info("%03d: Boom!",self.id)
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
                self.out_buffer_p = abs(info[0] - 1)
                self.out_buffer_n = info[1]
                self.data = self.out_buffer_p & self.out_buffer_n
                return info
        else:
            raise ValueError(f"Time is either tic or tock: {time}")


def test():
    """Node test"""
    # testing now done by pytest
    pass


if __name__ == "__main__":
    pass
