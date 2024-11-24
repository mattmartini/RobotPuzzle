"""Node for circular doubly linked list"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.0.5"

import logging
from rich import print

# from rich import inspect

logger = logging.getLogger(f"RobotLogger.{__name__}")


class Node:

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
        logger.info(f"Create node {self.id:03d}")

    def __repr__(self):
        """Node repr"""
        return f"Node({self.id:03d}, {self.active}, {self.data}, {self.prev.id:03d}, {self.next.id:03d})"

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
        # string += print("Hello from [bold magenta]robotpuzzle![/bold magenta]")

        return string

    def flush_output_buffers(self):
        """Send data to neighbors, clear outgoing buffers"""
        logger.debug(f"{self.id:03d}:    {self.prev.id:03d} <-- {self.out_buffer_p}")
        self.prev.in_buffer_n = self.out_buffer_p
        self.out_buffer_p = None

        logger.debug(f"{self.id:03d}:    {self.out_buffer_n} --> {self.next.id:03d}")
        self.next.in_buffer_p = self.out_buffer_n
        self.out_buffer_n = None

    def read_input_buffers(self):
        """Read and clear input buffers"""
        cur_buffers = [self.in_buffer_p, self.in_buffer_n]
        self.in_buffer_p = None
        self.in_buffer_n = None
        logger.debug(f"{self.id:03d}: input buffers {cur_buffers}")
        return cur_buffers

    def activate(self):
        """Activate Node"""
        self.active = 1
        logger.info(f"{self.id:03d}: Activated")

    def deactivate(self):
        """Deactivate Node"""
        self.active = 0
        logger.info(f"{self.id:03d}: Deactivated")

    def turn_inside_out_and_explode(self):
        """Explode"""
        explosion = f"{self.id:03d}: Boom!"
        print(explosion)
        logger.info(explosion)

    def take_action(self, time="tic"):
        """Action taken this tic or tock"""
        if time == "tic":
            logger.debug(f"{self.id:03d}: tic")
            if self.active == 0:
                return
            self.flush_output_buffers()
        elif time == "tock":
            logger.debug(f"{self.id:03d}: tock")
            info = self.read_input_buffers()
            if self.active == 0:
                if info == [None, None]:
                    return
                else:
                    self.activate
                    return
            else:
                """TODO set data and output+buffers"""
                """ decide on actions: explode or pass data """
                if info == [1, 1]:
                    self.turn_inside_out_and_explode()
                pass
        else:
            raise ValueError(f"Time is either tic to tock: {time}")


def test():
    """Node test"""
    Node.count = 0
    print("-------------------------------------------------------------------")
    print("-------------------------------------------------------------------")

    robotA = Node()
    robotB = Node()
    robotB.prev = robotA
    robotB.next = robotA
    robotA.prev = robotB
    robotA.next = robotB
    robotC = Node()
    robotC.prev = robotB
    robotC.next = robotA
    robotA.prev = robotC
    robotB.next = robotC
    # print(repr(robotC))
    # print(locals())
    # inspect(robotA, methods=True)
    logger.info("Create three robots")

    def show_robots():
        print(robotA)
        print(robotB)
        print(robotC)

    def time_click(time=0):
        robotA.take_action("tic")
        robotB.take_action("tic")
        robotC.take_action("tic")
        robotA.take_action("tock")
        robotB.take_action("tock")
        robotC.take_action("tock")
        show_robots()

    time_click(0)

    robotA.data = 1
    robotB.data = 1
    robotC.data = 0
    robotA.in_buffer_p = 1
    robotB.out_buffer_p = 1
    # print(inspect(robotB))
    robotB.activate()
    time_click(1)

    robotC.out_buffer_p = 7
    robotC.out_buffer_n = 8
    robotB.out_buffer_p = 5
    robotB.out_buffer_n = 6
    time_click(2)

    robotA.out_buffer_n = 1
    robotC.out_buffer_p = 1
    time_click(3)
    robotC.turn_inside_out_and_explode()


if __name__ == "__main__":
    test()
