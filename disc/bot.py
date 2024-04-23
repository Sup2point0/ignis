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
from .predict import Predict
from .play import play


__version__ = "1.0.0"


bot = commands.Bot(intents = disc.Intents.none())


def script():
  bot.remove_command("help")
  bot.add_cog(Config(bot))
  bot.add_cog(Load(bot))
  bot.add_cog(Predict(bot))
  bot.add_cog(play(bot))

  load_dotenv()
  link = os.getenv("LINK")
  if link is None:
    raise ValueError("missing materials for Link Summon!")
  
  bot.run(token = link)
