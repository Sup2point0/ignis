'''
Ai.
'''

import os

import nextcord as disc
from nextcord import Embed, SlashOption, SelectOption
from nextcord import ui
from nextcord.ui import View, Modal, button
from nextcord.ext import commands
from dotenv import load_dotenv

import suptools as sup
# from ignis import Ai
from .load import load


bot = commands.Bot(intents = disc.Intents.none())
bot.remove_command("help")


@ bot.slash_command(description = "testing")
async def test(ctx):
  await ctx.send("testing!", ephemeral = True,
    embed = Embed(title = "test", description = "testing\ntesting")
  )


def script():
  bot.add_cog(load(bot))

  load_dotenv()
  link = os.getenv("LINK")
  if link is None:
    raise ValueError("missing materials for Link Summon!")
  
  bot.run(token = link)
