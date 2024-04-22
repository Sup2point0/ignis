'''
Implements the `play` family of slash commands.
'''

import random

import nextcord as disc
from nextcord import Embed, SlashOption, SelectOption
from nextcord import ui, ButtonStyle
from nextcord.ui import Modal, button
from nextcord.ext import commands

import ygo


class play(commands.Cog):
  '''Commands involving playing games.'''

  def __init__(self, bot):
    self.bot = bot

    self.games = {
      "ygordle-word": None,
      "ygordle-card": None,
    }
    '''Games in progress.'''

  @ disc.slash_command()
  async def play(self, ctx):
    pass

  @ play.subcommand()
  async def ygordle(self, ctx):
    pass
  
  ## /play ygordle word ##
  @ ygordle.subcommand()
  async def word(self, ctx,
    characters: int = SlashOption(
      "characters", "the number of characters the word will contain (defaults to 5)",
      required = False, default = 5,
    ),
  ):
    '''play a game of ygordle where you guess a word'''

    if self.games["ygordle-word"]:
      await ctx.send("Sorry, game in progress!", ephemeral = True)
      return

    ## setup
    root = await ctx.send(embed = Embed(
      ...
    ))
    thread = await root.create_thread(name = "YGORDLE (word)", auto_archive_duration = 60)

    join = await thread.send(ctx.user.mention)
    await join.delete()

    self.games["ygordle-word"] = WordGame(chars = characters)

  class WordGame:
    def __init__(self, chars: int = 5):
      self.chars = chars
      
      self.live: bool = True
      self.guesses: list[tuple[str]] = []

  class WordView(ui.View):
    def __init__(self):
      super().__init__(timeout = None)

    @ button(label = "Cancel", style = ButtonStyle.danger, custom_id = "ygordle.word.cancel")
    async def cancel(self, button, ctx):
      pass

  ## /play ygordle card ##
