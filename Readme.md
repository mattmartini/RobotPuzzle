# Robot Puzzle

## The Problem
2^N$ (that's two raised to the power of N, where N can be arbitrarily large) robots are arranged shoulder to shoulder facing outwards in a circle. Each robot has limited memory - it can only remember O(1) bits of information, and can give or receive information only to the robot to its left and the robot to its right. Time proceeds in discrete rounds. In each round, each robot can communicate O(1) bits of information with the two robots to its right and left. Specifically, in each round, each robot sends O(1) bits to each of his neighboring robots, and then receives whatever bits those robots sent him or her. No robot knows in advance how many robots there are in the circle.

Initially, all robots are in a "waiting" state, in which they do nothing. At some round t (unknown in advance), a person presses a "go" button on one of the robots, activating that robot. In the next round, that robot communicates to its neighbors, activating them, and (as the time steps pass), the activated robots communicate with their neighbors, activating them in turn. All communication and robot state-changes happen according to some protocol that has been agreed upon and programmed into the robots in advance. Then, at some later time, all robots simultaneously self-destruct. (No robot self-destructs before this time.)

The challenge problem is to determine a protocol to program the robots with so that this will happen, subject to the constraints outlined above.

### example sol'n (non-working)
An example that doesn't quite work would be:

  (1) The first robot (the one that the person touches at time t), at time t+1 sends the message "1" to the robot to its right. At time t+2, that robot in turn sends the same message to the robot to its right, and so on. In general, each robot follows the protocol "if I receive message "1" from the left, then in the next round, I send the message "1" to my right."

  (2) While this is happening, the first robot counts the time steps as they pass. When, eventually, it receives the message from its left, it knows that the number of robots is equal to the number of time steps passed. Let this number be $2^N$. In the next round, the robot sends the following message to its right: "self-destruct after $2^N-1$ rounds." The recipient waits a round, then sends the following message to its right "self-destruct after $2^N-2$ rounds. In general, if a robot receives a message of the form "self-destruct after X rounds", then, in the next time step, it sends the following message to its right: "self-destruct after X-1 rounds". Also, each robot, after receiving a message of the form "self-destruct after X rounds", starts counting the rounds as they occur, and self-destructs once X more rounds have passed.

That's an example protocol, and it would allow the robots to self-destruct simultaneously. But it doesn't fit the criteria outlined for two reasons. First, it requires each robot to communicate more than O(1) bits of information in some rounds. (To communicate a number as large as $2^N$ requires N bits, and N can be arbitrarily large.) Second, it requires each robot (when counting down) to remember up to N bits of information.

The protocol you design must require each robot to remember, and to communicate, only O(1) bits of information at any given time, no matter how large N is! 
