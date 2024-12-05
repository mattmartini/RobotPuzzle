from rich import pretty, inspect, print
from robotpuzzle import node
from robotpuzzle import robots
from robotpuzzle import buffer

circle=robots.CDLL(2)
circle.create_robots()
inspect(circle)
