"""Test Fixtures"""

import pytest
from robotpuzzle.node import Node


@pytest.fixture(name="multi_node")
def fixture_new_node():
    """Returns a new node instance"""

    def _fixture_new_node():
        a_node = Node()
        return a_node

    return _fixture_new_node

@pytest.fixture(name="new_node")
def get_new_node():
    """Returns a new node instance"""
    return Node()

@pytest.fixture(name="session_node")
def fixture_session_node(scope="session"):
    """Returns a new session node instance"""
    return Node()
