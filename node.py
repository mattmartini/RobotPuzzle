"""Node for circular doubly linked list"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.0.4"

from rich import print
# from rich import inspect


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

    def __repr__(self):
        return f"Node({self.id}, {self.active}, {self.data}, {self.prev.id}, {self.next.id})"

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
    robotA.data = 1
    robotA.raction = 1
    robotA.lbuffer = 1
    # print(robotA)
    # print(repr(robotA))
    # print(locals())

    robotB = Node()
    robotB.prev = robotA
    robotB.next = robotA
    robotA.prev = robotB
    robotA.next = robotB
    robotB.data = 1
    robotB.active = 1
    robotB.raction = 1
    robotB.lbuffer = 0
    # print(robotB)
    # print(repr(robotB))
    # print(locals())

    robotC = Node()
    robotC.prev = robotB
    robotC.next = robotA
    robotA.prev = robotC
    robotB.next = robotC
    robotC.data = 0
    robotC.raction = 0
    robotC.lbuffer = 1
    # print(repr(robotC))
    # print(locals())
    # inspect(robotA, methods=True)

    print(robotA)
    print(robotB)
    print(robotC)


if __name__ == "__main__":
    test()
