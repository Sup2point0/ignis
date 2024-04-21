'''
Implements the `load` family of slash commands.
'''

import nextcord as disc
from nextcord.ext import commands


class load(commands.Cog):
  '''Commands involving loading data.'''

  def __init__(self, bot):
    self.bot = bot

  @ disc.slash_command()
  async def test(self, ctx):
    await ctx.response.send("testing!", ephemeral = True)
