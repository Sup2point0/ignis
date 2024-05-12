from typing import Optional as Opt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped as Mp
from sqlalchemy.orm import mapped_column as mc

from .card import Card


class CardArt(Card):
  __tablename__ = "CardArts"

  art_id: Mp[int] = mc(primary_key = True)

  # 1 of these must be provided
  monster_id = mc(ForeignKey("Monsters.card_id"), nullable = True)
  spelltrap_id = mc(ForeignKey("SpellTraps.card_id"), nullable = True)
  # ideally we could store it in a single `card_id` attribute but we'll have to get joined table inheritance working for that

  def __repr__(self):
    return f"CardArt(card = {self.monster_id or self.spelltrap_id} | id = {self.art_id})"
