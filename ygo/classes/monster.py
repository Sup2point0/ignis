from __future__ import annotations

from typing import Optional as Opt

import sqlalchemy as sqla
from sqlalchemy.orm import Mapped as Mp
from sqlalchemy.orm import mapped_column as mc

from .card import Card
from .art import CardArt


class MonsterCard(Card):
  '''A monster card and its table in the database.'''

  __tablename__ = "Monsters"

  card_id: Mp[int] = mc(primary_key = True)
  name: Mp[str]
  card_type: Mp[str]
  kind: Mp[str]
  race: Mp[str]
  '''The monster Type, such as Dragon or Cyberse.'''
  attribute: Mp[str]
  level: Mp[str]
  attack: Mp[int]
  defense: Mp[Opt[int]]
  is_effect: Mp[bool]
  is_pend: Mp[bool]

  def __repr__(self):
    return f"Card(id = {self.card_id} | name = {self.name} | type = {self.card_type} | info = {self.race}/{self.attribute.upper()}/Lv{self.level}/ATK {self.attack}/DEF {self.defense})"

  @ staticmethod
  def from_json(data: dict) -> tuple[MonsterCard, CardArt]:
    '''Create a card with data in a JSON `dict` from the YGOPRODECK API.'''

    card_type = Card.sanitise_type(data["type"])

    return MonsterCard(
      card_id = data["id"],
      name = data["name"],
      card_type = card_type,
      kind = data["frameType".split("_")[0]].lower(),
      race = data["race"].lower(),
      attribute = data["attribute"].upper(),
      level = data.get("level", data.get("linkval")),
      attack = data["atk"],
      defense = data.get("def", None),
      is_effect = ("effect" in data["type"].casefold()),
      is_pend = ("pendulum" in data["frameType"].casefold()),
    )
