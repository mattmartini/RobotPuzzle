"""Circular doubly linked list"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.3.1"

from rich.columns import Columns
from robotpuzzle.node import Node
from robotpuzzle import log
from robotpuzzle.console import console


class CDLL:
    """CDLL class: Circle of Robots"""

    def __init__(self, num=0):
        """Initalize CDLL"""
        self.num = num
        self.robots_needed = 2**self.num
        self.count = 0
        self.head = None
        self.time = 0
        self.logger = log.get_logger()
        self.logger.debug("Create CDLL N=%d", self.num)

    def __del__(self):
        """Delete Node"""
        self.logger.debug("Delete CDLL %03d", self.num)

    def __repr__(self):
        """Print the CDLL"""
        string = ""

        if self.head is None:
            string += "Circular Doubly Linked List Empty"
            return string

        string += f"Circular Doubly Linked List:\n{self.head.data}"
        temp = self.head.next
        while temp != self.head:
            string += f" -> {temp.data}"
            temp = temp.next
        return string

    def append(self, data=None):
        """Append a node"""
        self.insert(self.count, data)
        self.logger.info("Append a Node")

    def insert(self, index, data=None):
        """Insert a node"""
        if (index > self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")

        if self.count == self.robots_needed:
            raise ValueError(
                f"Too many robots: needed: {self.robots_needed}, size: {self.count}"
            )

        if self.head is None:
            self.head = Node(data)
            self.count = 1
            return

        temp = self.head
        if index == 0:
            temp = temp.prev
        else:
            for _ in range(index - 1):
                temp = temp.next

        temp.next.prev = Node(data)
        temp.next.prev.next, temp.next.prev.prev = temp.next, temp
        temp.next = temp.next.prev
        if index == 0:
            self.head = self.head.prev
        self.count += 1
        self.logger.info("Insert a Node")
        return

    def get(self, index):
        """Return the node at the index"""
        if (index >= self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def size(self):
        """Number of nodes in the list"""
        return self.count

    def run_clock(self):
        """Run the clock (tic & tock) for each robot"""
        self.logger.info("Run the clock - time: %04d", self.time)
        robot = self.head
        for _ in range(self.count):
            self.logger.debug("%03d - tic", robot.id)
            robot.take_action("tic")
            robot = robot.next
        for _ in range(self.count):
            self.logger.debug("%03d - tock", robot.id)
            robot.take_action("tock")
            robot = robot.next
        self.time += 1

    def show_circle(self):
        """Print the robot nodes"""
        robot = self.head
        console.rule("Circle of Robots")
        robot_circle = []
        for _ in range(self.count):
            robot_circle.append(robot.node_panel())
            robot = robot.next
        console.print(Columns(robot_circle))

    def create_robots(self):
        """Create circle of robots"""
        for _ in range(self.robots_needed):
            self.append()


def test():
    """Test CDLL"""
    # testing now done by pytest
    pass


def main():
    """Robots Main"""

    console.print("Hello from [bold magenta]robotpuzzle![/bold magenta]")
    robots = CDLL(3)
    robots.create_robots()
    robots.logger.info("---------------- New Main Run ----------------")


if __name__ == "__main__":
    main()
