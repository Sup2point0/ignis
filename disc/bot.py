'''
Ai.
'''

import os

import nextcord as disc
from nextcord.ext import commands
from dotenv import load_dotenv

import suptools as sup
# from ignis import Ai
from .load import load


__version__ = "1.0.0"


bot = commands.Bot(intents = disc.Intents.none())


def script():
  bot.remove_command("help")
  bot.add_cog(load(bot))

  load_dotenv()
  link = os.getenv("LINK")
  if link is None:
    raise ValueError("missing materials for Link Summon!")
  
  bot.run(token = link)
