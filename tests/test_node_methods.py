"""Tests for: Node for circular doubly linked list"""

import pytest
from robotpuzzle.node import Node


@pytest.mark.node
def test_node_class_get_count(new_node):
    """Test class getter"""
    assert new_node.count == Node.count


@pytest.mark.node
def test_node_class_count_inc(multi_node):
    """Test class Node counter is incremented after each new node"""
    cur_count = Node.count
    node_a = multi_node()
    assert node_a.id == cur_count
    node_b = multi_node()
    assert node_b.id == cur_count + 1
    node_c = multi_node()
    assert node_c.id == cur_count + 2


@pytest.mark.node
def test_activate(new_node):
    """Test that activate method activates node"""
    assert new_node.active is False
    new_node.activate()
    assert new_node.active is True


@pytest.mark.node
def test_deactivate(new_node):
    """Test that activate method activates node"""
    assert new_node.active is False
    new_node.activate()
    assert new_node.active is True
    new_node.deactivate()
    assert new_node.active is False


@pytest.mark.node
def test_turn_inside_out_and_explode(new_node):
    """Test that node explodes"""
    cur_count = f"{Node.count - 1:03d}"
    assert new_node.turn_inside_out_and_explode() == f"{cur_count}: Boom!"


@pytest.mark.node
def test_flush_output_buffers(new_node):
    """Test output buffers sent to neighbors, buffers flushed"""
    assert new_node.buffers.input["prev"] is None
    assert new_node.buffers.input["next"] is None
    assert new_node.buffers.output["prev"] is None
    assert new_node.buffers.output["next"] is None
    new_node.buffers.output["prev"] = 3
    new_node.buffers.output["next"] = 7
    assert new_node.buffers.output["prev"] == 3
    assert new_node.buffers.output["next"] == 7
    new_node.flush_output_buffers()
    assert new_node.buffers.input["prev"] == 7
    assert new_node.buffers.input["next"] == 3
    assert new_node.buffers.output["prev"] is None
    assert new_node.buffers.output["next"] is None


@pytest.mark.node
def test_read_input_buffers(new_node):
    """Test input buffers from to neighbors, buffers flushed"""
    assert new_node.buffers.input["prev"] is None
    assert new_node.buffers.input["next"] is None
    new_node.buffers.input["prev"] = 9
    new_node.buffers.input["next"] = 2
    assert new_node.buffers.input["prev"] == 9
    assert new_node.buffers.input["next"] == 2
    buffers = new_node.read_input_buffers()
    assert buffers[0] == 9
    assert buffers[1] == 2
    assert new_node.buffers.input["prev"] is None
    assert new_node.buffers.input["next"] is None


@pytest.mark.node
def test_advance_clock(new_node):
    """Test take action neither tic nor tock"""
    with pytest.raises(ValueError) as e:
        new_node.advance_clock()
    assert "Time is either tic or tock" in str(e.value)


@pytest.mark.node
def test_advance_clock_tic(new_node):
    """Test take action tic"""
    assert new_node.active == 0
    returned = new_node.advance_clock("tic")
    assert returned is None
    new_node.activate()
    new_node.buffers.output["prev"] = 4
    new_node.buffers.output["next"] = 5
    assert new_node.buffers.output["prev"] == 4
    assert new_node.buffers.output["next"] == 5
    returned = new_node.advance_clock("tic")
    assert new_node.buffers.input["prev"] == 5
    assert new_node.buffers.input["next"] == 4
    assert new_node.buffers.output["prev"] is None
    assert new_node.buffers.output["next"] is None


@pytest.mark.node
def test_advance_clock_tock(new_node):
    """Test take action tock"""
    assert new_node.active == 0
    returned = new_node.advance_clock("tock")
    assert returned is None
    assert new_node.buffers.input["prev"] is None
    assert new_node.buffers.input["next"] is None
    new_node.buffers.input["prev"] = 1
    new_node.buffers.input["next"] = 5
    returned = new_node.advance_clock("tock")
    assert new_node.active == 1
    assert new_node.buffers.input["prev"] is None
    assert new_node.buffers.input["next"] is None
    new_node.buffers.input["prev"] = 1
    new_node.buffers.input["next"] = 1
    returned = new_node.advance_clock("tock")
