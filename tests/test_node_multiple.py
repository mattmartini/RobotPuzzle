"""Tests for: Multiple Nodes for circular doubly linked list"""

import pytest


@pytest.mark.node
@pytest.mark.multi
def test_nodes(multi_node):
    """Test multiple nodes"""

    def show_robots(robots):
        for robot in robots:
            print(robot)

    def time_click(robots):
        for robot in robots:
            robot.take_action("tic")
        for robot in robots:
            in_buff = robot.take_action("tock")
            print(in_buff)
        show_robots(robots)

    robot_a = multi_node()
    robot_b = multi_node()
    robot_b.prev = robot_a
    robot_b.next = robot_a
    robot_a.prev = robot_b
    robot_a.next = robot_b
    print(robot_a)
    print(robot_b)
    robot_c = multi_node()
    robot_c.prev = robot_b
    robot_c.next = robot_a
    robot_a.prev = robot_c
    robot_b.next = robot_c

    robots = [robot_a, robot_b, robot_c]

    robot_a.data = 5
    robot_b.data = 3
    robot_c.data = 1


    robot_a.in_buffer_n = 2
    robot_a.in_buffer_p = 4
    robot_c.in_buffer_p = 6
    robot_c.in_buffer_n = 8
    robot_b.in_buffer_n = 3
    robot_a.out_buffer_p = 1
    robot_a.out_buffer_n = 3
    robot_b.out_buffer_p = 5
    robot_b.out_buffer_n = 7
    robot_c.out_buffer_p = 0
    robot_c.out_buffer_n = 9
    show_robots(robots)
    time_click(robots)
    assert robot_a.in_buffer_n is None
    assert robot_a.in_buffer_p is None
    time_click(robots)
    assert robot_a.out_buffer_n == 5
    assert robot_a.out_buffer_p == 8
    time_click(robots)
    assert robot_a.out_buffer_n == 2
    assert robot_a.out_buffer_p == 0
    time_click(robots)
    assert robot_a.out_buffer_n == 4
    assert robot_a.out_buffer_p == 7
    robot_c.out_buffer_p = 1
    robot_a.out_buffer_n = 1
    time_click(robots)
    assert robot_a.out_buffer_n == 1
    assert robot_a.out_buffer_p == 1
    time_click(robots)
    assert robot_a.out_buffer_n == 0
    assert robot_a.out_buffer_p == 6


