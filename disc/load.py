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


class Load(commands.Cog):
  '''Commands involving loading data.'''

  colours = {
    "spell": 0x3d8776,
    "trap": 0x9c3775,
    "normal": 0x000,
    "effect": 0xae603a,
    "ritual": 0x526faf,
    "fusion": 0x773f8a,
    "synchro": 0xe0deda,
    "xyz": 0x000103,
    "link": 0x3e8ac6,
  }

  presets = {
    "card-id": SlashOption(
      "id", "ID (password) of the card",
      required = False, default = None,
    ),
    "card-name": SlashOption(
      "card", "name of the card",
      required = False, default = None,
    ),
  }

  def __init__(self, bot):
    self.bot = bot


  ## utils ##
  class CardNotFound(Exception):
    '''Exception raised when a card is not found.'''
    pass

  async def _find_(self, ctx, constraints: str = None, rand = False) -> list:
    '''Try to find a card from the database.
    
    If none is found, send an error message and raise `CardNotFound`.
    '''

    await ctx.response.defer()

    data = ygo.sql.load_monsters_data(constraints)

    if not data:
      await ctx.send("No card found!", ephemeral = True)
      raise Load.CardNotFound()
    
    return random.choice(data) if rand else data[0]


  ## /load ##
  @ disc.slash_command()
  async def load(self, ctx):
    pass


  ## /load card ##
  @ load.subcommand()
  async def card(self, ctx):
    pass

  @ card.subcommand(name = "with-id")
  async def card_with_id(self, ctx, card: int = presets["card-id"]):
    '''load info for a card from the database, searching by ID'''

    found = await self._find_(ctx,
      constraints = f"id = {card}" if card else None,
      rand = not card
    )

    await self._send_card_details_(ctx, found)

  @ card.subcommand(name = "with-name")
  async def card_with_name(self, ctx, card: str = presets["card-name"]):
    '''load info for a card from the database, searching by name'''

    found = await self._find_(ctx, 
      constraints = f"name = {card}" if card else None,
      rand = not card
    )

  async def _send_card_details_(self, ctx, card):
    '''Send the details of a card.'''

    await ctx.send(embed = (
      Embed(
        title = card["name"],
        url = ygo.link.url(card),
        colour = Load.colours[card["kind"].lower()],
      )
      # .set_thumbnail(url = disc.File())
      .add_field(name = "Type", value = card["race"])
      .add_field(name = "Kind", value = card["kind"])
      .add_field(name = "Attribute", value = card["attribute"])
      .add_field(name = "Level", value = card["level"])
      .add_field(name = "ATK", value = card["attack"])
      .add_field(name = "DEF", value = card["defense"])
      .set_footer(text = "data sourced from the YGOPRODECK API")
    ))


  ## /load art ##
  @ load.subcommand()
  async def art(self, ctx):
    pass

  @ art.subcommand(name = "with-id")
  async def art_with_id(self, ctx, card: int = presets["card-id"]):
    '''load art for a card from the database, given its ID'''

    found = await self._find_(ctx,
      constraints = f"id = {card}" if card else None,
      rand = not card
    )
    
    await ctx.send(
      file = disc.File(BytesIO(found["art"]),
      filename = card["name"] + ".jpg")
    )


  ## autofill /load ##
  @ card_with_id.on_autocomplete("card")
  async def fill_card_id(self, ctx, card):
    q = f"id LIKE '{card}'"
    await self._autofill_(ctx, q)
  
  @ card_with_name.on_autocomplete("card")
  async def fill_card_name(self, ctx, card):
    q = f"name LIKE '%{card}%'"
    await self._autofill_(ctx, q)

  async def _autofill_(self, ctx, query: str):
    '''Query the database to autofill a slash command.'''
    
    cards = ygo.sql.load_monsters_data(query)
    out = [f'''{card["id"]} – {card["name"]}''' for card in cards[:13]]

    await ctx.response.send_autocomplete(out)
