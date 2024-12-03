"""Test for: Circular doubly linked list"""

import pytest


@pytest.mark.initial
@pytest.mark.robots
def test_initial_empty_count(empty_circle):
    """Test CDLL initial count"""
    assert empty_circle.count == 0


@pytest.mark.initial
@pytest.mark.robots
def test_initial_repr(empty_circle):
    """Test initial repr"""
    assert "Doubly Circular Linked List" in str(repr(empty_circle))


@pytest.mark.initial
@pytest.mark.robots
def test_initial_empty_head(empty_circle):
    """Test CDLL initial head"""
    assert empty_circle.head is None


@pytest.mark.initial
@pytest.mark.robots
def test_initial_empty_num(empty_circle):
    """Test CDLL initial num"""
    assert empty_circle.num == 0


@pytest.mark.initial
@pytest.mark.robots
def test_initial_empty_robots_needed(empty_circle):
    """Test CDLL initial robots needed"""
    assert empty_circle.robots_needed == 1


@pytest.mark.initial
@pytest.mark.robots
def test_initial_empty_time(empty_circle):
    """Test CDLL initial time"""
    assert empty_circle.time == 0


@pytest.mark.initial
@pytest.mark.robots
def test_initial_count(new_circle):
    """Test CDLL initial count"""
    a_circle = new_circle(3)
    assert a_circle.count == 0


@pytest.mark.initial
@pytest.mark.robots
def test_initial_head(new_circle):
    """Test CDLL initial head"""
    a_circle = new_circle(3)
    assert a_circle.head is None


@pytest.mark.initial
@pytest.mark.robots
def test_initial_num(new_circle):
    """Test CDLL initial num"""
    a_circle = new_circle(3)
    assert a_circle.num == 3


@pytest.mark.initial
@pytest.mark.robots
def test_initial_robots_needed(new_circle):
    """Test CDLL initial robots needed"""
    a_circle = new_circle(3)
    assert a_circle.robots_needed == 8


@pytest.mark.initial
@pytest.mark.robots
def test_initial_time(new_circle):
    """Test CDLL initial time"""
    a_circle = new_circle(3)
    assert a_circle.time == 0
