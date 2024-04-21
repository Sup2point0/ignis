'''
Ai.
'''

import os

import nextcord as disc
from nextcord import Embed, SlashOption, SelectOption
from nextcord import ui
from nextcord.ui import View, Modal, button
from nextcord.ext import commands

import suptools as sup
from ignis import Ai
from .load import load


bot = commands.Bot(intents = disc.Intents.all())
bot.remove_command("help")


@ bot.slash_command(description = "testing")
async def test(interaction):
  await interaction.response.send("testing!", ephemeral = True)


def script():
  bot.add_cog(load(bot))
  
  bot.run(os.getenv("LINK"))


if __name__ == "__main__":
  sup.run(script, vitals = True)
