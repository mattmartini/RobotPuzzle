from rich import pretty, inspect, print
import node
import robots
import buffer
a=node.Node()
b=buffer.Buffer()
c=robots.CDLL(2)
c.create_robots()
inspect(a)
inspect(b)
inspect(c)
