"""Tests for: Multiple Nodes for circular doubly linked list"""

import pytest

@pytest.mark.xfail
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


    robot_a.buffers.input["next"] = 2
    robot_a.buffers.input["prev"] = 4
    robot_c.buffers.input["prev"] = 6
    robot_c.buffers.input["next"] = 8
    robot_b.buffers.input["next"] = 3
    robot_a.buffers.output["prev"] = 1
    robot_a.buffers.output["next"] = 3
    robot_b.buffers.output["prev"] = 5
    robot_b.buffers.output["next"] = 7
    robot_c.buffers.output["prev"] = 0
    robot_c.buffers.output["next"] = 9
    show_robots(robots)
    time_click(robots)
    assert robot_a.buffers.input["next"] is None
    assert robot_a.buffers.input["prev"] is None
    time_click(robots)
    assert robot_a.buffers.output["next"] == 5
    assert robot_a.buffers.output["prev"] == 8
    time_click(robots)
    assert robot_a.buffers.output["next"] == 2
    assert robot_a.buffers.output["prev"] == 0
    time_click(robots)
    assert robot_a.buffers.output["next"] == 4
    assert robot_a.buffers.output["prev"] == 7
    robot_c.buffers.output["prev"] = 1
    robot_a.buffers.output["next"] = 1
    time_click(robots)
    assert robot_a.buffers.output["next"] == 1
    assert robot_a.buffers.output["prev"] == 1
    time_click(robots)
    assert robot_a.buffers.output["next"] == 0
    assert robot_a.buffers.output["prev"] == 6
    robot_d = multi_node()
    print(robot_d.buffers)
    robot_d.buffers.input["prev"] = 4
    robot_d.buffers.input["next"] = 3
    robot_d.buffers.output["prev"] = 2
    robot_d.buffers.output["next"] = 1
    print(robot_d.buffers)

