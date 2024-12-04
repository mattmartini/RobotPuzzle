"""Tests for: Buffer for Node"""

import pytest


@pytest.mark.initial
@pytest.mark.buffer
def test_initial_repr(new_buffer):
    """Test initial repr"""
    assert repr(new_buffer) == "Buffer(input:[ None, None ], output:[ None, None ])"


@pytest.mark.initial
@pytest.mark.buffer
def test_initial_input(new_buffer):
    """Test initial input"""
    assert new_buffer.input["prev"] is None
    assert new_buffer.input["next"] is None


@pytest.mark.initial
@pytest.mark.buffer
def test_initial_output(new_buffer):
    """Test initial output"""
    assert new_buffer.output["prev"] is None
    assert new_buffer.output["next"] is None
