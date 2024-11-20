"""Node for circular doubly linked list"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.0.0"


class Node:
    def __init__(self, data=None):
        """Initalize Node"""
        self.id = None
        self.active = 0
        self.data = data
        self.prev = None
        self.next = None
        self.rbuffer = None
        self.lbuffer = None
        self.raction = None
        self.laction = None

    def __repr__(self):
        """Print the Node"""
        string = "╭─────────╮\n"
        string += f"│   {self.id:03d}   │\n"

        string += f"│  {(self.lbuffer, '_')[self.lbuffer is None]} "
        string += f"{(self.data, '_')[self.data is None]} "
        string += f"{(self.rbuffer, '_')[self.rbuffer is None]}  │\n"

        string += f"│{(self.laction, '_')[self.laction is None]}"
        string += "<-- -->"
        string += f"{(self.raction, '_')[self.raction is None]}│\n"
        string += "╰─────────╯\n"

        return string

    def action(self):
        """Action taken this tic tock"""
        pass
        """ activate ? """
        """ check buffers and register """
        """ decide on actions: explode or pass data """


def test():
    """Node test"""
    robot = Node()
    robot.id = 3
    robot.data = 1
    robot.raction = 1
    robot.lbuffer = 1
    print(robot)


if __name__ == "__main__":
    test()
