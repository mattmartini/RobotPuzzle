"""Tests for: Node for circular doubly linked list"""

import pytest
from robotpuzzle.node import Node


@pytest.fixture
def get_node():
    """Get a node"""
    robot = Node()
    return robot


def test_active(get_node):
    """Test action"""
    assert get_node.active == 0


def test_data(get_node):
    """Test data"""
    assert get_node.data is None


def test_buffers(get_node):
    """Test data"""
    assert get_node.data is None
    assert get_node.in_buffer_p is None
    assert get_node.in_buffer_n is None
    assert get_node.out_buffer_p is None
    assert get_node.out_buffer_n is None
