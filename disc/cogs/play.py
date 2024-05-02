'''
Implements the `play` family of slash commands.
'''

from __future__ import annotations

import random

import nextcord as disc
from nextcord import Embed, SlashOption, SelectOption
from nextcord import ui, ButtonStyle
from nextcord.ui import Modal, button
from nextcord.ext import commands

import ygo
from .. import dyna
from ..resources import colours


class Play(commands.Cog):
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
    # characters: int = SlashOption(
    #   "characters", "the number of characters the word will contain (defaults to 5)",
    #   required = False, default = 5,
    # ),
  ):
    '''play a game of ygordle where you guess a word'''

    if isinstance(interaction, disc.Thread):
      await ctx.send(dyna.punctuate("Can’t play a game in a thread"), ephemeral = True)
      return
    if isinstance(interaction, disc.DMChannel):
      await ctx.send(dyna.punctuate("Can’t play a game in direct messages"))
      return
    if self.games["ygordle-word"]:
      await ctx.send(dyna.punctuate("Sorry, game in progress"), ephemeral = True)
      return

    embed = Play.WordEmbed().set_footer(text = "Initialising...")
    view = Play.WordView()
    root = await ctx.send(embed = embed, view = view)
    
    thread = await root.create_thread(name = "YGORDLE (word)", auto_archive_duration = 60)
    join = await thread.send(ctx.user.mention)
    await join.delete()

    game = Play.WordGame()
    self.games["ygordle-word"] = game

    await root.edit(embed = embed.set_footer(text = "Ongoing"))
    await self.run_ygordle_word(game, thread)

  class WordEmbed(Embed):
    def __init__(desc = "", *, player: disc.User):
      self.player = player
      self.reset(desc = desc)

    def reset(desc: str):
      self.title = "YGORDLE (word)"
      self.description = desc
      self.colour = colours.pink.nova
      self.set_footer(text = "Synchronising...")
      self.set_author(name = self.player.display_name, icon_url = self.player.avatar.url)

  class WordView(ui.View):
    '''The view for a word YGORDLE root message.'''
    
    def __init__(self):
      super().__init__(timeout = None)

    @ button(label = "Cancel", style = ButtonStyle.danger, custom_id = "ygordle.word.cancel")
    async def cancel(self, button, ctx):
      pass

  class WordGame:
    '''A word YGORDLE game instance.'''
    
    def __init__(self, chars: int = 5):
      self.chars = chars
      
      self.live: bool = True
      self.done: bool = False
      self.guesses: list[tuple[str]] = []

  async def run_ygordle_word(self, game: Play.WordGame, thread: disc.Thread):
    '''Run the game loop of word YGORDLE.'''

    while not game.done:
      

  ## /play ygordle card ##
