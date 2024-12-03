"""Test for: Circular doubly linked list"""

import pytest


@pytest.mark.robots
def test_circles(new_circle):
    """Test CDLL scenario"""
    a_circle = new_circle(3)
    a_circle.create_robots()
    a_circle.show_circle()
    a_circle.logger.error("bleep blorp")

