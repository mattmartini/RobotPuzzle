"""Tests for: Node for circular doubly linked list"""

import pytest
from robotpuzzle.node import Node


@pytest.mark.initial
@pytest.mark.node
def test_initial_repr(new_node):
    """Test initial repr"""
    cur_count = f"{Node.count - 1:03d}"
    assert repr(new_node) == f"Node({cur_count}, False, None, {cur_count}, {cur_count})"


@pytest.mark.initial
@pytest.mark.node
def test_initial_id(new_node):
    """Test initial id"""
    assert new_node.id == Node.count - 1


@pytest.mark.initial
@pytest.mark.node
def test_initial_active(new_node):
    """Test action"""
    assert new_node.active is False


@pytest.mark.initial
@pytest.mark.node
def test_initial_data(new_node):
    """Test data"""
    assert new_node.data is None


@pytest.mark.initial
@pytest.mark.node
def test_initial_prev(new_node):
    """Test pointer to prev node"""
    assert new_node.prev is new_node


@pytest.mark.initial
@pytest.mark.node
def test_initial_next(new_node):
    """Test pointer to next node"""
    assert new_node.next is new_node


@pytest.mark.initial
@pytest.mark.node
def test_initial_buffers(new_node):
    """Test data"""
    assert new_node.data is None
    assert new_node.buffers.input["prev"] is None
    assert new_node.buffers.input["next"] is None
    assert new_node.buffers.output["prev"] is None
    assert new_node.buffers.output["next"] is None
