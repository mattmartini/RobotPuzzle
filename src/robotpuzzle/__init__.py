"""RobotPuzzle Init"""

__date__ = '2024-12-05'
__version__ = "1.4.0"

from rich import inspect
from robotpuzzle import node
from robotpuzzle import circles
from robotpuzzle import buffer


def main() -> None:
    print("Hello from robot puzzle!")
    circle=circles.CDLL(2)
    circle.create_robots()
    inspect(circle)
    circle.show_circle()

    for seconds in range(2):
        circle.run_clock()
        circle.show_circle()

    circle.head.activate()
    circle.head.buffers.set_outputs(0,0)

    for seconds in range(6):
        circle.run_clock()
        circle.show_circle()
