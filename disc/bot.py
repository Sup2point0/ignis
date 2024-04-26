'''
Ai.
'''

import os
import traceback

import nextcord as disc
from nextcord import Embed
from nextcord.ext import commands
from dotenv import load_dotenv

import suptools as sup
from .cogs import cogs
from . import dyna
# from ignis import Ai


def script():
  # run this first, since some cogs depend on environment variables
  load_dotenv()

  bot = commands.Bot(intents = disc.Intents.none())
  bot.__version__ = "1.1.0"
  
  bot.remove_command("help")
  for cog in cogs:
    bot.add_cog(cog(bot))

  link = os.getenv("LINK")
  if link is None:
    raise ValueError("missing materials for Link Summon!")
  
  bot.run(token = link)
