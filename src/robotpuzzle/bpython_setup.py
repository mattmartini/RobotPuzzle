from rich import pretty, inspect, print
from robotpuzzle import node
from robotpuzzle import circles
from robotpuzzle import buffer

circle=circles.CDLL(2)
circle.create_robots()
inspect(circle)
