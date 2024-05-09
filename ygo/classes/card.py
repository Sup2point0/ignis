from __future__ import annotations

from typing import Optional as Opt

import sqlalchemy as sqla
from sqlalchemy.orm import Mapped as Mp
from sqlalchemy.orm import mapped_column as mc

from .base import Base


class Card(Base):
  __tablename__ = "cards"

  card_id: Mp[int] = mc(primary_key = True)
  name: Mp[str]
  card_type: Mp[str]
  kind: Mp[str]
  race: Mp[str]
  attribute: Mp[str]
  level: Mp[str]
  attack: Mp[Opt[int]]
  defense: Mp[Opt[int]]
  is_effect: Mp[bool]
  is_pend: Mp[bool]

  def __repr__(self):
    return f"Card(id = {self.card_id} | name = {self.name} | type = {self.card_type} | info = {self.race}/{self.attribute.upper()}/Lv{self.level}/ATK {self.attack}/DEF {self.defense})"

  @ staticmethod
  def sanitise_type(text: str) -> str:
    text = text.casefold()

    if "monster" in text:
      return "monster"
    if "spell" in text:
      return "spell"
    if "trap" in text:
      return "trap"
  
  @ staticmethod
  def from_dict(data: dict) -> Card:
    '''Create a card with data in a JSON `dict` from the YGOPRODECK API.'''

    return Card(
      card_id = data["id"],
      name = data["name"],
      type = Card._sanitise_type_(data["type"]),
      kind = data["frameType".split("_")[0]].lower(),
      race = data["race"].lower(),
      attribute = data["attribute"].upper(),
      level = data.get("level", data.get("linkval")),
      attack = data["atk"],
      defense = data.get("def", None),
      pend = ("pendulum" in data["frameType"].lower()),
    )
