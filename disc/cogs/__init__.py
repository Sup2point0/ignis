'''
Implements the slash commands.
'''

from .error import Error
from .config import Config
from .discover import Discover
from .load import Load
from .play import Play
from .predict import Predict

cogs = [Error, Config, Discover, Load, Play, Predict]
