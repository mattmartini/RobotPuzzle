"""Tests for: Node for circular doubly linked list"""

import pytest
from robotpuzzle.node import Node


def test_initial_repr(new_node):
    """Test initial repr"""
    cur_count = f"{Node.count - 1:03d}"
    assert repr(new_node) == f"Node({cur_count}, 0, None, {cur_count}, {cur_count})"


def test_initial_id(new_node):
    """Test initial id"""
    assert new_node.id == Node.count - 1


def test_initial_active(new_node):
    """Test action"""
    assert new_node.active == 0


def test_initial_data(new_node):
    """Test data"""
    assert new_node.data is None


def test_initial_prev(new_node):
    """Test pointer to prev node"""
    assert new_node.prev is new_node


def test_initial_next(new_node):
    """Test pointer to next node"""
    assert new_node.next is new_node


def test_initial_buffers(new_node):
    """Test data"""
    assert new_node.data is None
    assert new_node.in_buffer_p is None
    assert new_node.in_buffer_n is None
    assert new_node.out_buffer_p is None
    assert new_node.out_buffer_n is None


def test_activate(new_node):
    """Test that activate method activates node"""
    assert new_node.active == 0
    new_node.activate()
    assert new_node.active == 1


def test_deactivate(new_node):
    """Test that activate method activates node"""
    assert new_node.active == 0
    new_node.activate()
    assert new_node.active == 1
    new_node.deactivate()
    assert new_node.active == 0


def test_turn_inside_out_and_explode(new_node):
    """Test that node explodes"""
    cur_count = f"{Node.count - 1:03d}"
    assert new_node.turn_inside_out_and_explode() == f"{cur_count}: Boom!"
