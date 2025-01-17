"""Rich Console"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.4.2"

from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.columns import Columns

robot_theme = Theme(
    {
        "buffer": "plum2",
        "active_node": "chartreuse3",
        "inactive_node": "dark_khaki",
        "explosion": "light_goldenrod1 on red1",
    }
)

console = Console(theme=robot_theme)
