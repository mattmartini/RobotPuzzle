"""Tests for: Node for circular doubly linked list"""

# import pytest
from robotpuzzle.node import Node
import robotpuzzle.log


def test_active():
    """Test action"""
    robot_a = Node()
    assert robot_a.active == 0
