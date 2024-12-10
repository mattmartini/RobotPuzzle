# Robot Puzzle

## Project
This project was built to help me bush up on python skills, and acquaint
myself with the `uv` package manager in preparation for developing a
Mushroom environmental controller based on the
[Greenhouse](https://github.com/mattmartini/Greenhouse) ([Greenhouse
Wiki](https://github.com/mattmartini/Greenhouse/wiki)) envirnmental
controller. It also seemed like a fun problem to solve.

## The Problem
[Origin of Puzzle](http://www.cs.ucr.edu/~neal/puzzles)  
2^N$ (that's two raised to the power of N, where N can be arbitrarily
large) robots are arranged shoulder to shoulder facing outwards in a
circle. Each robot has limited memory - it can only remember O(1) bits
of information, and can give or receive information only to the robot to
its left and the robot to its right. Time proceeds in discrete rounds.
In each round, each robot can communicate O(1) bits of information with
the two robots to its right and left. Specifically, in each round, each
robot sends O(1) bits to each of his neighboring robots, and then
receives whatever bits those robots sent him or her. No robot knows in
advance how many robots there are in the circle.

Initially, all robots are in a "waiting" state, in which they do
nothing. At some round t (unknown in advance), a person presses a "go"
button on one of the robots, activating that robot. In the next round,
that robot communicates to its neighbors, activating them, and (as the
time steps pass), the activated robots communicate with their neighbors,
activating them in turn. All communication and robot state-changes
happen according to some protocol that has been agreed upon and
programmed into the robots in advance. Then, at some later time, all
robots simultaneously self-destruct. (No robot self-destructs before
this time.)

The challenge problem is to determine a protocol to program the
robots with so that this will happen, subject to the constraints
outlined above.

### example sol'n (non-working)
An example that doesn't quite work would be:

  (1) The first robot (the one that the person touches at time t), at
      time t+1 sends the message "1" to the robot to its right. At time
      t+2, that robot in turn sends the same message to the robot to its
      right, and so on. In general, each robot follows the protocol "if
      I receive message "1" from the left, then in the next round, I
      send the message "1" to my right."

  (2) While this is happening, the first robot counts the time steps as
      they pass. When, eventually, it receives the message from its
      left, it knows that the number of robots is equal to the number of
      time steps passed. Let this number be $2^N$. In the next round,
      the robot sends the following message to its right: "self-destruct
      after $2^N-1$ rounds." The recipient waits a round, then sends the
      following message to its right "self-destruct after $2^N-2$
      rounds. In general, if a robot receives a message of the form "self-
      destruct after X rounds", then, in the next time step, it sends
      the following message to its right: "self-destruct after X-1
      rounds". Also, each robot, after receiving a message of the form
      "self-destruct after X rounds", starts counting the rounds as they
      occur, and self-destructs once X more rounds have passed.

That's an example protocol, and it would allow the robots to self-
destruct simultaneously. But it doesn't fit the criteria outlined for
two reasons. First, it requires each robot to communicate more than O(1)
bits of information in some rounds. (To communicate a number as large as
$2^N$ requires N bits, and N can be arbitrarily large.) Second, it
requires each robot (when counting down) to remember up to N bits of
information.

The protocol you design must require each robot to remember, and to
communicate, only O(1) bits of information at any given time, no matter
how large N is!

## Simulation
This project creates a simulator for the robot puzzle to test out
algorithms for the puzzle's solution. There are classes for the robots
(nodes) and the circle of robots (Circular Doubly Linked List).

Each unit of time takes two discrete parts a `tic` and a `tock`. During the
`tic` phase all of the robots send a 0 or 1 (or nothing) to one or both of
its neighbors. Then on the `tock` it receives what its neighbors sent it
and decides what to do in the next round. It has a 1 bit data register
that can be changed once each clock cycle.

### Robots
Each robot (node) has an `id`, pointer to its `prev`ious and `next`
neighbor, an `active` flag, a (O)1 bid `data` register, and `buffers`
for incoming and outgoing data.

### Legend
To help visualize what is going on with the robots, each robot is represented by a panel as follows.

```
     ╭─────────────────╮
     │003  - 000 -  001│   
     │_<-- _  _  _ -->_│  
     ╰─────────────────╯
```
In the first line are shown:
 prev   active   node number    active   next  
the following line shows:  prev_out_buf  <-- prev_in_buf   data  next_in_buf --> next_out_buf


## Solution
Given that there are always 2^N Robots, we will always have a starting
robot (head) and its mirror (tail) that is halfway around the circle.

There are two obvious ways of starting (to my mind): 
1. On "Go" the head robot sends a 0 or 1 to the next node, which in
       turn sends this same datum to its next node, ... Eventually, the head
       node will receive data on its prev node input buffer. At this
       point it will realize that it is "head" and know that all of the
       other robots are now active.
2. On "Go" the head robot sends a 0 or 1 to both of its neighbors
       activating them. Each of these robots then passes the datum on to
       its respective neighbor (head's next sends to it's next,...).
       Upon receiving data from both its prev and next neighbors at the
       same time the robot will realize that it is "tail" and also that
       all of the robots are now active.
Not sure which of these will be more helpful.

All robots run the same code. Any can be "head" (or "tail") as the "Go"
robot is chosen at random. The "head" robot will not "remember" that it
is "head," unless this info is stored in `data`

It is interesting to note that while each robot can only remember (O)1
bit there are actually there possibilities of what it can send its
neighbor on each clock cycle: 0, 1, or Null (None).

### Details

### versions

The version schema for this project is major.minor.patch (ie 1.2.3)
`bump-my-version` is used to manage the changes.
```
bump-my version show-bump
bump-my version bump patch
bump-my version bump minor
bump-my version bump major
```
