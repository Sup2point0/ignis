'''
Ai.
'''

import os

import nextcord as disc
from nextcord.ext import commands
from dotenv import load_dotenv

import suptools as sup
# from ignis import Ai
from .config import Config
from .load import Load
from .discover import Discover
from .predict import Predict
from .play import Play


__version__ = "1.0.0"

bot = commands.Bot(intents = disc.Intents.none())


def script():
  load_dotenv()
  # run this first, since some cogs depend on environment variables

  bot.remove_command("help")

  cogs = [Config, Load, Discover, Predict, Play]
  for cog in cogs:
    bot.add_cog(cog(bot))

  link = os.getenv("LINK")
  if link is None:
    raise ValueError("missing materials for Link Summon!")
  
  bot.run(token = link)
