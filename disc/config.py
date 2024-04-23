'''
Implements the `config` admin and debug slash commands.
'''

import sys

import nextcord as disc
from nextcord.ext import commands


class Config(commands.Cog):
  '''Commands involving playing games.'''

  def __init__(self, bot):
    self.bot = bot

  @ disc.slash_command()
  async def config(self, ctx):
    pass

  @ config.subcommand()
  async def kill(self, ctx):
    '''kill the bot'''

    await ctx.send("killing the bot...", ephemeral = True)
    await self.bot.close()
    sys.exit()
