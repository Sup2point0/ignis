'''
Implements the `load` family of slash commands.
'''

import random
from io import BytesIO
from typing import Iterable, Callable

import nextcord as disc
from nextcord import Embed, SlashOption, SelectOption
from nextcord import ui
from nextcord.ui import View, Modal, button
from nextcord.ext import commands

import config
import ygo


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
    '''No card was found.'''

  async def _find_(self, ctx,
    constraints: Iterable[Callable] = [],
    rand = False,
  ) -> ygo.Card:
    '''Try to find a card from the database.
    
    If none is found, send an error message and raise `CardNotFound`.
    '''

    await ctx.response.defer()

    monsters = ygo.sql.load(ygo.MonsterCard, constraints)
    spelltraps = ygo.sql.load(ygo.SpellTrapCard, constraints)
    found = (monsters or spelltraps)

    if not found:
      await ctx.send("No card found!", ephemeral = True)
      raise Load.CardNotFound()
    
    if rand:
      return random.choice(found)
    else:
      return found[0]


  ## /load ##
  @ disc.slash_command()
  async def load(self, ctx):
    pass

  @ load.subcommand(name = "with-id")
  async def with_id(self, ctx,
    card: int = presets["card-id"],
    art: bool = SlashOption(
      "art-only", "whether to load only the art image",
      required = False, default = False,
    ),
  ):
    '''load info for a card from the database, searching by ID'''

    found = await self._find_(ctx,
      constraints = lambda: ygo.MonsterCard.card_id == card,
      rand = not card
    )

    await self._send_card_details_(ctx, found, art)

  @ load.subcommand(name = "with-name")
  async def with_name(self, ctx,
    card: str = presets["card-name"],
    art: bool = SlashOption(
      "art-only", "whether to load only the art image",
      required = False, default = False,
    ),
  ):
    '''load info for a card from the database, searching by name'''

    found = await self._find_(ctx, 
      constraints = lambda: ygo.MonsterCard.name == card,
      rand = not card
    )

    await self._send_card_details_(ctx, found, art)

  async def _send_card_details_(self, ctx, card: ygo.MonsterCard, art: ygo.CardArt):
    '''Send the details or art of a card.'''

    if art:
      with open(config.ROOT / f"assets/images{card.art_id}.jpg") as file:
        await ctx.send(
          file = file,
          filename = card.name + ".jpg",
        )

    else:
      await ctx.send(embed = (
        Embed(
          title = card.name,
          url = ygo.api.fetch_card_url(card),
          colour = Load.colours[card.kind.lower()],
        )
        # .set_thumbnail(url = disc.File())
        .add_field(name = "Password", value = card.card_id)
        .add_field(name = "Kind", value = card.kind)
        .add_field(name = "Type", value = card.race)
        .add_field(name = "Attribute", value = card.attribute)
        .add_field(name = "Level", value = card.level)
        .add_field(name = "ATK", value = card.attack)
        .add_field(name = "DEF", value = card.defense)
        .set_footer(text = "data sourced from the YGOPRODECK API")
      ))


  ## autofill /load ##
  @ with_id.on_autocomplete("card")
  async def fill_card_id(self, ctx, card):
    q = f"id LIKE '{card}'"
    await self._autofill_(ctx, q)
  
  @ with_name.on_autocomplete("card")
  async def fill_card_name(self, ctx, card):
    q = f"name LIKE '%{card}%'"
    await self._autofill_(ctx, q)

  async def _autofill_(self, ctx, query: str):
    '''Query the database to autofill a slash command.'''
    
    cards = ygo.sql.load_monsters_data(query)
    out = [f'''{card["id"]} – {card["name"]}''' for card in cards[:12]]

    await ctx.response.send_autocomplete(out)
