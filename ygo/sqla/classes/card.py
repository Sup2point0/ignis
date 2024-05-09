from typing import Optional as Opt

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
