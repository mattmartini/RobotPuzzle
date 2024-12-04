"""Tests for: Buffer for Node"""

import pytest
from robotpuzzle.buffer import Buffer


@pytest.mark.buffer
def test_get_inputs(new_buffer):
    """Test get_inputs"""
    assert new_buffer.get_inputs() == [None, None]
    new_buffer.input["prev"] = 3
    new_buffer.input["next"] = 5
    assert new_buffer.get_inputs() == [3, 5]
    print(new_buffer)

@pytest.mark.buffer
def test_set_inputs(new_buffer):
    """Test set_inputs"""
    new_buffer.set_inputs(7,9)
    assert new_buffer.get_inputs() == [7, 9]
    new_buffer.set_inputs(pre=1,nex=6)
    assert new_buffer.get_inputs() == [1, 6]
    new_buffer.logger.debug(new_buffer.get_inputs())
    print(new_buffer)


@pytest.mark.buffer
def test_get_outputs(new_buffer):
    """Test get_outputs"""
    assert new_buffer.get_outputs() == [None, None]
    new_buffer.output["prev"] = 2
    new_buffer.output["next"] = 6
    assert new_buffer.get_outputs() == [2, 6]
    print(new_buffer)

@pytest.mark.buffer
def test_set_outputs(new_buffer):
    """Test set_outputs"""
    new_buffer.set_outputs(4,8)
    assert new_buffer.get_outputs() == [4, 8]
    new_buffer.set_outputs(pre=0,nex=6)
    assert new_buffer.get_outputs() == [0, 6]
    new_buffer.logger.debug(new_buffer.get_outputs())
    print(new_buffer)


