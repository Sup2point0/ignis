'''
Implements the `load` family of slash commands.
'''

import random
from io import BytesIO

import nextcord as disc
from nextcord import Embed, SlashOption, SelectOption
from nextcord import ui
from nextcord.ui import View, Modal, button
from nextcord.ext import commands

import ygo
from .silence import silence


class load(commands.Cog):
  '''Commands involving loading data.'''

  def __init__(self, bot):
    self.bot = bot

  class CardNotFound(Exception):
    '''Exception raised when a card is not found.'''
    pass

  @ staticmethod
  async def find(ctx, constraints: str = None, rand = False) -> list:
    '''Try to find a card from the database.
    
    If none is found, send an error message and raise `CardNotFound`.
    '''

    await ctx.response.defer()

    data = ygo.sql.load_monsters_data(constraints)

    if not data:
      await ctx.send("No card found!", ephemeral = True)
      raise load.CardNotFound()
    
    return random.choice(data) if rand else data[0]

  @ disc.slash_command()
  async def load(self, ctx):
    pass

  ## /load card ##
  @ load.subcommand()
  async def card(self, ctx):
    pass

  @ card.subcommand(name = "with-id")
  async def card_with_id(self, ctx,
    card: int = SlashOption(
      "card", "ID (password) of the card",
      required = False, default = None
    ),
  ):
    '''load info for a card from the database, given its ID'''

    found = await load.find(ctx,
      constraints = f"id = {card}" if card else None,
      rand = not card
    )
    
    await ctx.send(embed = (
      Embed(
        title = found["name"],
        url = ygo.link.url(found["name"]),
        colour = 0x000,
      )
      .set_thumbnail(url = disc.File(BytesIO(found["art"])))
      .add_field(name = "Type", value = found["race"])
      .add_field(name = "Kind", value = found["kind"])
      .add_field(name = "Attribute", value = found["attribute"])
      .add_field(name = "Level", value = found["level"])
      .add_field(name = "ATK", value = found["attack"])
      .add_field(name = "DEF", value = found["defense"])
      .set_footer(text = "data sourced from the YGOPRODECK API")
    ))

  ## /load art ##
  @ load.subcommand()
  async def art(self, ctx):
    pass

  @ art.subcommand(name = "with-id")
  async def art_with_id(self, ctx,
    card: int = SlashOption(
      "id", "ID (password) of the card",
      required = False, default = None,
    ),
  ):
    '''load art for a card from the database, given its ID'''

    found = await load.find(ctx,
      constraints = f"id = {card}" if card else None,
      rand = not card
    )
    
    await ctx.send(
      file = disc.File(BytesIO(found["art"]),
      filename = card["name"] + ".jpg")
    )
