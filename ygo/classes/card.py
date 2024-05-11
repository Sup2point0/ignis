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
  race: Mp[str]
  '''Either the monster type or the Spell/Trap property.'''

  ## MONSTER-EXCLUSIVE ##
  kind: Mp[Opt[str]]
  attribute: Mp[Opt[str]]
  level: Mp[Opt[str]]
  attack: Mp[Opt[int]]
  defense: Mp[Opt[int]]
  is_effect: Mp[Opt[bool]]
  is_pend: Mp[Opt[bool]]

  def __repr__(self):
    return (
      f"Card(id = {self.card_id} | name = {self.name} | type = {self.card_type} " + (
        f"| info = {self.race}/{self.attribute.upper()}/Lv{self.level}/ATK {self.attack}/DEF {self.defense}"
        if self.card_type == "monster" else
        f"| property = {self.race}"
      ) + ")"
    )

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

    card_type = Card.sanitise_type(data["type"])

    return Card(
      card_id = data["id"],
      name = data["name"],
      card_type = card_type,
      race = data["race"].lower(),
      **({
        "kind": data["frameType".split("_")[0]].lower(),
        "attribute": data["attribute"].upper(),
        "level": data.get("level", data.get("linkval")),
        "attack": data["atk"],
        "defense": data.get("def", None),
        "is_effect": ("effect" in data["type"].casefold()),
        "is_pend": ("pendulum" in data["frameType"].casefold()),
      } if card_type == "monster" else {})
    )
