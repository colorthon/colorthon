# programmer Mmdrza.Com
from .Text import Color


class console():
    def __init__(self):
        self.red = Color.red
        self.green = Color.green
        self.yellow = Color.yellow
        self.cyan = Color.cyan
        self.blue = Color.blue
        self.white = Color.white
        self.grey = Color.grey
        self.magenta = Color.magenta
        self.reset = Color.reset


__version__: str = "v4.6.3"
__license__: str = "MIT"
__author__: str = "Mohammadreza Fekri"
__email__: str = "PyMmdrza@gmail.com"
__description__: str = "Fast And Easy Generated Wallet on Python With Blockthon"

__all__: list = [
    "__version__",
    "__license__",
    "__author__",
    "__email__",
    "__description__",
    "utils",
    "Text"
]
