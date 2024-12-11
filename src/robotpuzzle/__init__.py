"""RobotPuzzle Init"""

__date__ = "2024-12-05"
__version__ = "1.4.0"

from rich import inspect
from robotpuzzle import circles

N = 2
MAX_PRE_TIME = 2

# The pre-time (before "Go" is pressed) should be a random number
# For dev a value of 2 should suffice


def main() -> None:
    """Robot Puzzle Main"""
    print("Hello from robot puzzle!")
    circle = circles.CDLL(N)
    circle.create_robots()
    inspect(circle)
    circle.show_circle()

    # run the clock before "Go" is pressed (pre_time)
    for _ in range(MAX_PRE_TIME):
        circle.run_clock()
        circle.show_circle()

    # "Go" pressed.  Activates head.
    # Should activate a random robot.
    # (actually make a random robot head and activate it.)
    circle.head.activate()
    circle.head.buffers.set_outputs(0, 0)

    # run the clock
    # should be a while true that runs until Boom!
    for _ in range(6):
        circle.run_clock()
        circle.show_circle()
