"""Circular doubly linked list"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.0.5"

from node import Node
from rich import print
from rich import inspect


class CDLL:

    def __init__(self, num=0):
        """Initalize CDLL"""
        self.num = num
        self.robots_needed = 2**self.num
        self.count = 0
        self.head = None
        self.time = 0

    def __repr__(self):
        """Print the CDLL"""
        string = ""

        if self.head is None:
            string += "Doubly Circular Linked List Empty"
            return string

        string += f"Doubly Circular Linked List:\n{self.head.data}"
        temp = self.head.next
        while temp != self.head:
            string += f" -> {temp.data}"
            temp = temp.next
        return string

    def append(self, data=None):
        """Append a node"""
        self.insert(self.count, data)
        return

    def insert(self, index, data=None):
        """Insert a node"""
        if (index > self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")

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
        return

    def get(self, index):
        """Return the node at the index"""
        if (index >= self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.data

    def size(self):
        """Number of nodes in the list"""
        return self.count

    def show_circle(self):
        """Print the robot nodes"""
        temp = self.head
        for _ in range(self.count):
            print(temp)
            temp = temp.next

    def create_robots(self):
        """Create circle of robots"""
        for _ in range(self.robots_needed):
            self.append()


def test():
    """Test CDLL"""
    print("-------------------------------------------------------------------")
    robots = CDLL(3)
    robots.insert(0)
    robots.insert(1)
    robots.append()
    inspect(robots, methods=True)
    robots.show_circle()

    bots = CDLL(2)
    bots.create_robots()
    inspect(bots, methods=True)
    bots.show_circle()


def main():
    print("Hello from [bold magenta]robotpuzzle![/bold magenta]")
    robots = CDLL(3)
    robots.create_robots()


if __name__ == "__main__":
    test()
