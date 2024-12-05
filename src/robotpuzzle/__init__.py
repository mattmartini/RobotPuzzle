"""RobotPuzzle Init"""

__date__ = "2024-12-04"
__version__ = "1.3.0"

from rich import pretty, inspect, print
from robotpuzzle import node
from robotpuzzle import robots
from robotpuzzle import buffer


def main() -> None:
    print("Hello from robot puzzle!")
    circle=robots.CDLL(2)
    circle.create_robots()
    inspect(circle)
    circle.show_circle()

    for seconds in range(2):
        circle.run_clock()
        circle.show_circle()

    circle.head.activate()
    circle.head.buffers.set_outputs(0,0)

    for seconds in range(16):
        circle.run_clock()
        circle.show_circle()
