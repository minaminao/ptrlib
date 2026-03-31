import sys

if sys.platform.startswith("linux"):
    from .debug import *
    from .process import *
