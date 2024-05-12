from __future__ import annotations

from typing import Optional as Opt

import sqlalchemy as sqla
from sqlalchemy.orm import Mapped as Mp
from sqlalchemy.orm import mapped_column as mc

from .card import Card
from .art import CardArt


class SpellTrap(Card):
  '''A Spell or Trap card.'''

  __tablename__ = "SpellTraps"

  card_id: Mp[int] = mc(primary_key = True)
  name: Mp[str]
  card_type: Mp[str]
  property: Mp[str]
  
  def __repr__(self):
    return (
      f"Card(id = {self.card_id} | name = {self.name} | type = {self.card_type} " + (
        f"| info = {self.race}/{self.attribute.upper()}/Lv{self.level}/ATK {self.attack}/DEF {self.defense}"
        if self.card_type == "monster" else
        f"| property = {self.race}"
      ) + ")"
    )
  
  @ staticmethod
  def from_dict(data: dict) -> tuple[Card, CardArt]:
    '''Create a card with data in a JSON `dict` from the YGOPRODECK API.'''

    card_type = Card.sanitise_type(data["type"])

    return Card(
      card_id = data["id"],
      name = data["name"],
      card_type = card_type,
      property = data["race"].lower()
    )
