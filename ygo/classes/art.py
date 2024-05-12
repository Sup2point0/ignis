from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped as Mp
from sqlalchemy.orm import mapped_column as mc


class Base(DeclarativeBase):
  pass


class CardArt(Base):
  __tablename__ = "CardArts"

  art_id: Mp[int] = mc(primary_key = True)
  card_id = mc(ForeignKey("cards.card_id"))
  url: Mp[str]

  def __repr__(self):
    return f"CardArt(card = {self.card_id} | id = {self.art_id} | url = {self.url})"
