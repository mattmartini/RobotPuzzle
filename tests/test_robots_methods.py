"""Test for: Circular doubly linked list"""

import pytest


@pytest.mark.robots
def test_insert_out_of_range(new_circle):
    """Test CDLL insert out of range"""
    a_circle = new_circle(2)
    with pytest.raises(ValueError) as e:
        a_circle.insert(-1)
    assert "Index out of range" in str(e.value)
    with pytest.raises(ValueError) as e:
        a_circle.insert(9999)
    assert "Index out of range" in str(e.value)


@pytest.mark.robots
def test_insert_too_many_robots(new_circle):
    """Test CDLL insert out of range"""
    a_circle = new_circle(0)
    a_circle.append()
    with pytest.raises(ValueError) as e:
        a_circle.append()
    assert "Too many robots" in str(e.value)
    a_circle = new_circle(3)
    a_circle.create_robots()
    with pytest.raises(ValueError) as e:
        a_circle.append()
    assert "Too many robots" in str(e.value)


@pytest.mark.robots
def test_insert(new_circle):
    """Test CDLL insert"""
    a_circle = new_circle(2)
    a_circle.insert(0)
    assert a_circle.count == 1
    assert a_circle.head is not None
    assert a_circle.head.id == a_circle.head.prev.id
    assert a_circle.head.id == a_circle.head.next.id
    a_circle.insert(1)
    assert a_circle.count == 2
    assert a_circle.head is not None
    assert a_circle.head.prev.id == a_circle.head.next.id
    assert a_circle.head.prev.next.id == a_circle.head.next.prev.id
    a_circle.insert(2)
    assert a_circle.count == 3
    assert a_circle.head is not None
    assert a_circle.head.prev.next.id == a_circle.head.next.prev.id


@pytest.mark.robots
def test_append(new_circle):
    """Test CDLL insert"""
    a_circle = new_circle(3)
    assert a_circle.head is None
    a_circle.append()
    assert a_circle.count == 1
    assert a_circle.head is not None
    a_circle.append()
    assert a_circle.count == 2
    assert a_circle.head is not None


@pytest.mark.robots
def test_get_out_of_range(new_circle):
    """Test CDLL get out of range"""
    a_circle = new_circle(2)
    with pytest.raises(ValueError) as e:
        a_circle.get(-1)
    assert "Index out of range" in str(e.value)
    with pytest.raises(ValueError) as e:
        a_circle.get(9999)
    assert "Index out of range" in str(e.value)


@pytest.mark.robots
def test_get(new_circle):
    """Test CDLL get"""
    a_circle = new_circle(3)
    a_circle.append()
    assert a_circle.head == a_circle.get(0)
    a_circle.append()
    assert a_circle.head.next == a_circle.get(1)
    assert a_circle.head.prev == a_circle.get(1)
    a_circle.append()
    assert a_circle.head.next.next == a_circle.get(2)
    assert a_circle.head.prev == a_circle.get(2)
    a_circle.append()
    assert a_circle.head.next.next.next == a_circle.get(3)
    assert a_circle.head.prev == a_circle.get(3)


@pytest.mark.robots
def test_size(new_circle):
    """Test CDLL size"""
    a_circle = new_circle(3)
    assert a_circle.size() == a_circle.count
    a_circle.append()
    assert a_circle.size() == a_circle.count

@pytest.mark.robots
def test_create_robots(new_circle):
    """Test CDLL create robots"""
    a_circle = new_circle(3)
    a_circle.create_robots()
    assert a_circle.size() == a_circle.robots_needed
    a_circle.show_circle()


