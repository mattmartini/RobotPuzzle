"""Node for circular doubly linked list"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.0.0"

from rich import print
from rich import inspect


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
        self.rbuffer = None
        self.lbuffer = None
        self.raction = None
        self.laction = None

    def __repr__(self):
        return f"Node({self.id}, {self.active}, {self.data}, {self.prev.id}, {self.next.id})"

    def __str__(self):
        """Print the Node"""
        string = "╭────────────────╮\n"
        string += f"│       {self.id:03d}      │\n"

        string += f"│{(self.laction, '_')[self.laction is None]}<--"
        string += f"  {(self.lbuffer, '_')[self.lbuffer is None]} "
        string += f"{(self.data, '_')[self.data is None]} "
        string += f"{(self.rbuffer, '_')[self.rbuffer is None]} "
        string += f"-->{(self.raction, '_')[self.raction is None]}│\n"

        string += "╰────────────────╯\n"
        # string += print("Hello from [bold magenta]robotpuzzle![/bold magenta]")

        return string

    def action(self):
        """Action taken this tic tock"""
        pass
        """ activate ? """
        """ check buffers and register """
        """ decide on actions: explode or pass data """


def test():
    """Node test"""
    print("-------------------------------------------------------------------")
    robotA = Node()
    print(repr(robotA))
    robotA.data = 1
    robotA.raction = 1
    robotA.lbuffer = 1
    print(robotA)
    print(repr(robotA))
    print(locals())

    robotB = Node()
    robotB.prev = robotA
    robotB.next = robotA
    robotA.prev = robotB
    robotA.next = robotB
    robotB.data = 1
    robotB.raction = 1
    robotB.lbuffer = 0
    print(robotB)
    print(repr(robotB))
    print(locals())

    robotC = Node()
    robotC.prev = robotB
    robotC.next = robotA
    robotA.prev = robotC
    robotB.next = robotC
    robotC.data = 0
    robotC.raction = 0
    robotC.lbuffer = 1
    print(robotC)
    print(repr(robotC))
    print(locals())
    inspect(robotA, methods=True)


if __name__ == "__main__":
    test()
