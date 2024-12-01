"""Tests for: Node for circular doubly linked list"""

import pytest
from robotpuzzle.node import Node


@pytest.mark.initial
@pytest.mark.node
def test_initial_repr(new_node):
    """Test initial repr"""
    cur_count = f"{Node.count - 1:03d}"
    assert repr(new_node) == f"Node({cur_count}, 0, None, {cur_count}, {cur_count})"


@pytest.mark.initial
@pytest.mark.node
def test_initial_id(new_node):
    """Test initial id"""
    assert new_node.id == Node.count - 1


@pytest.mark.initial
@pytest.mark.node
def test_initial_active(new_node):
    """Test action"""
    assert new_node.active == 0


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
    assert new_node.in_buffer_p is None
    assert new_node.in_buffer_n is None
    assert new_node.out_buffer_p is None
    assert new_node.out_buffer_n is None


@pytest.mark.node
def test_node_class_count_inc(new_node):
    """Test class Node counter is incremented after each new node"""
    cur_count = Node.count - 1
    node_a = new_node
    assert node_a.id == cur_count
    node_b = Node()
    assert node_b.id == cur_count + 1
    node_c = Node()
    assert node_c.id == cur_count + 2


@pytest.mark.node
def test_activate(new_node):
    """Test that activate method activates node"""
    assert new_node.active == 0
    new_node.activate()
    assert new_node.active == 1


@pytest.mark.node
def test_deactivate(new_node):
    """Test that activate method activates node"""
    assert new_node.active == 0
    new_node.activate()
    assert new_node.active == 1
    new_node.deactivate()
    assert new_node.active == 0


@pytest.mark.node
def test_turn_inside_out_and_explode(new_node):
    """Test that node explodes"""
    cur_count = f"{Node.count - 1:03d}"
    assert new_node.turn_inside_out_and_explode() == f"{cur_count}: Boom!"


@pytest.mark.node
def test_flush_output_buffers(new_node):
    """Test output buffers sent to neighbors, buffers flushed"""
    assert new_node.in_buffer_p is None
    assert new_node.in_buffer_n is None
    assert new_node.out_buffer_p is None
    assert new_node.out_buffer_n is None
    new_node.out_buffer_p = 3
    new_node.out_buffer_n = 7
    assert new_node.out_buffer_p == 3
    assert new_node.out_buffer_n == 7
    new_node.flush_output_buffers()
    assert new_node.in_buffer_p == 7
    assert new_node.in_buffer_n == 3
    assert new_node.out_buffer_p is None
    assert new_node.out_buffer_n is None


@pytest.mark.node
def test_read_input_buffers(new_node):
    """Test input buffers from to neighbors, buffers flushed"""
    assert new_node.in_buffer_p is None
    assert new_node.in_buffer_n is None
    new_node.in_buffer_p = 9
    new_node.in_buffer_n = 2
    assert new_node.in_buffer_p == 9
    assert new_node.in_buffer_n == 2
    buffers = new_node.read_input_buffers()
    assert buffers[0] == 9
    assert buffers[1] == 2
    assert new_node.in_buffer_p is None
    assert new_node.in_buffer_n is None


@pytest.mark.node
def test_take_action_no_time(new_node):
    """Test take action neither tic nor tock"""
    with pytest.raises(ValueError) as e:
        new_node.take_action()
    assert "Time is either tic or tock" in str(e.value)


@pytest.mark.node
def test_take_action_tic(new_node):
    """Test take action tic"""
    assert new_node.active == 0
    returned = new_node.take_action("tic")
    assert returned is None
    new_node.activate()
    new_node.out_buffer_p = 4
    new_node.out_buffer_n = 5
    assert new_node.out_buffer_p == 4
    assert new_node.out_buffer_n == 5
    returned = new_node.take_action("tic")
    assert new_node.in_buffer_p == 5
    assert new_node.in_buffer_n == 4
    assert new_node.out_buffer_p is None
    assert new_node.out_buffer_n is None

@pytest.mark.node
def test_take_action_tock(new_node):
    """Test take action tock"""
    assert new_node.active == 0
    returned = new_node.take_action("tock")
    assert returned is None
    assert new_node.in_buffer_p is None
    assert new_node.in_buffer_n is None
    new_node.in_buffer_p = 1
    new_node.in_buffer_n = 5
    returned = new_node.take_action("tock")
    assert new_node.active == 1
    assert new_node.in_buffer_p is None
    assert new_node.in_buffer_n is None
    new_node.in_buffer_p = 1
    new_node.in_buffer_n = 1
    returned = new_node.take_action("tock")


