'''
Implements the `play` family of slash commands.
'''

from __future__ import annotations

import asyncio
import pathlib
import random

import nextcord as disc
from nextcord import Embed, SlashOption, SelectOption
from nextcord import ui, ButtonStyle
from nextcord.ui import Modal, button
from nextcord.ext import commands

import ygo
from .. import dyna
from ..resources import colours
from .error import ExceptionResponse


class Play(commands.Cog):
  '''Commands involving playing games.'''

  ROUTE = pathlib.Path(__file__).absolute().parents[2].joinpath("assets/data")

  def __init__(self, bot):
    self.bot = bot

    self.games = {
      "ygordle-word": None,
      "ygordle-card": None,
    }
    '''Games in progress.'''


  ## utils ##
  class GameEmbed(Embed):
    '''An embed sent as the root message where game threads are created.'''
    
    def __init__(self, game: str, *, player: disc.User):
      super().__init__()
      
      self.title = game
      self.description = ""
      self.colour = colours.games[game.casefold()]
      self.set_footer(text = "Initialising...")
      self.set_author(name = player.display_name, icon_url = player.avatar.url)

    def set_desc(self, content: str) -> Play.GameEmbed:
      '''Set description of embed and return the modified instance.'''

      self.description = content
      return self


  @ disc.slash_command()
  async def play(self, ctx):
    pass

  @ play.subcommand()
  async def ygordle(self, ctx):
    pass
  

  ## /play ygordle word ##
  @ ygordle.subcommand()
  async def word(self, ctx,
    # chars: int = SlashOption(
    #   "characters", "the number of characters the word will contain (defaults to 5)",
    #   required = False, default = 5,
    # ),
    tries: int = SlashOption(
      "attempts", "the number of tries you have to guess the word",
      required = False, default = 6,
    ),
  ):
    '''play a game of ygordle where you guess a word'''

    if isinstance(ctx.channel, disc.Thread):
      await ctx.send(dyna.punctuate("Can’t play a game in a thread"), ephemeral = True)
      return
    if isinstance(ctx.channel, disc.DMChannel):
      await ctx.send(dyna.punctuate("Can’t play a game in direct messages"))
      return
    if self.games["ygordle-word"]:
      await ctx.send(dyna.punctuate("Sorry, game in progress"), ephemeral = True)
      return

    game = Play.WordGame(tries = tries)#, chars = chars)
    self.games["ygordle-word"] = game

    embed = Play.GameEmbed("YGORDLE (word)", player = ctx.user)
    view = Play.WordView(game)
    root = await ctx.send(embed = embed, view = view)

    game.word = self.pick_ygordle_word("ygordle-words-5L")
    
    thread = await root.create_thread(name = "YGORDLE (word)", auto_archive_duration = 60)
    join = await thread.send(ctx.user.mention)
    await join.delete()

    await root.edit(embed = embed.set_footer(text = "Ongoing"))
    await self.run_ygordle_word(ctx, game, thread)

    await root.edit(embed = embed.set_footer(text = "Finished"))

  def pick_ygordle_word(self, source: str):
    '''Pick a random word from a given word list name.'''

    path = Play.ROUTE.joinpath(f"{source}.txt")

    with open(path) as file:
      return random.choice([line.strip() for line in file])

  async def run_ygordle_word(self, ctx, game: Play.WordGame, thread: disc.Thread):
    '''Run the game loop of word YGORDLE.'''

    while game.live:
      try:
        guess = await self.wait_for_guess(ctx, "message", thread)

        if guess is None:
          game.live = False
          break

        content = guess.content.strip()
        if len(content) < game.chars:
          raise ExceptionResponse(desc = f"Your guess needs to be at least {game.chars} letters.")
        
        guess = content.casefold().split()[0]
        letters = list(guess)
        if len(letters) > game.chars:
          raise ExceptionResponse(desc = f"Your guess cannot be more than {game.chars} letters.")
        
        accuracy = self.evaluate_guess(game, letters)
        
        game.guesses.append(guess)

      except ExceptionResponse as e:
        await thread.send(dyna.punctuate(e.desc))

  async def wait_for_guess(self, ctx, type, channel, timeout = 180):
    '''Wait for a guess in a thread.'''

    try:
      return await ctx.bot.wait_for(type, timeout = timeout,
        check = (lambda message: message.channel == channel and message.author == ctx.author)
      )
    except asyncio.TimeoutError:
      return None
    
  def evaluate_guess(self, game: Play.WordGame, guess: list[str]) -> dict[str, str]:
    '''Evaluate the correctness of the letters in a guess.'''

    # dicts preserve order, so this is fine
    return {
      letter:
        "precise" if game.word[i] == letter else
        "accurate" if letter in game.word else
        None
      for i, letter in enumerate(guess)
    }


  class WordView(ui.View):
    '''The view for a word YGORDLE root message.'''
    
    def __init__(self, game):
      self.game = game
      super().__init__(timeout = None)

    @ button(label = "Cancel", style = ButtonStyle.danger, custom_id = "ygordle.word.cancel")
    async def cancel(self, button, ctx):
      self.game.live = False

  class WordGame:
    '''A word YGORDLE game instance.'''
    
    def __init__(self, tries = 6, chars = 5):
      self.tries = tries
      self.chars = chars
      
      self.live: bool = True
      self.guesses: list[tuple[str]] = []
      

  ## /play ygordle card ##
