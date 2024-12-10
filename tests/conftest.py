"""Test Fixtures"""

import pytest
from robotpuzzle.buffer import Buffer
from robotpuzzle.node import Node
from robotpuzzle.circles import CDLL


@pytest.fixture(name="new_buffer")
def get_new_buffer():
    """Returns a new buffer instance"""
    return Buffer()


@pytest.fixture(name="new_node")
def get_new_node():
    """Returns a new node instance"""
    return Node()


@pytest.fixture(name="session_node")
def fixture_session_node(scope="session"):
    """Returns a new session node instance"""
    return Node()


@pytest.fixture(name="multi_node")
def fixture_new_node():
    """Returns a new node instance function"""

    def _fixture_new_node():
        a_node = Node()
        return a_node

    return _fixture_new_node


@pytest.fixture(name="empty_circle")
def get_empty_circle():
    """Returns a new empty circle instance"""
    return CDLL()


@pytest.fixture(name="new_circle")
def get_new_circle(num=0):
    """Returns a new circle instance function"""

    def _get_new_circle(num):
        a_circle = CDLL(num)
        return a_circle

    return _get_new_circle
