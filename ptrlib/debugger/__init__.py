import sys

if sys.platform.startswith("linux"):
    from .unix import *
