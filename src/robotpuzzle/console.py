"""Rich Console"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.3.1"

from rich.console import Console
from rich.theme import Theme

robot_theme = Theme(
    {
        "buffer": "plum2",
        "active_node": "chartreuse3",
        "inactive_node": "dark_khaki",
        "explosion": "light_goldenrod1 on red1",
    }
)

console = Console(theme=robot_theme)
