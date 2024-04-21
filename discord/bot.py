'''
Ai, the Discord bot.
'''

import os

import nextcord as disc
from nextcord import Embed, SlashOption, SelectOption
from nextcord import ui
from nextcord.ui import View, Modal, button
from nextcord.ext import commands

from ignis import Ai


bot = commands.Bot(intents = disc.Intents.all())
bot.remove_command("help")


@ bot.slash_command(description = "testing")
async def test(interaction):
  await interaction.response.send("testing!", ephemeral = True)


if __name__ == "__main__":
  bot.run(os.getenv("LINK"))
