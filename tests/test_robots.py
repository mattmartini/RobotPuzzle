"""Test for: Circular doubly linked list"""

# import pytest
from robotpuzzle.robots import CDLL
import robotpuzzle.log

import sys

# with open("/tmp/python-sys-path.txt", "w") as outfile:
#     outfile.write(str(sys.path))


def test_size():
    """test active"""
    return
    robot_cicrle = CDLL(3)
    assert robot_cicrle.size == 1
