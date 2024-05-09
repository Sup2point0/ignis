import sqlalchemy as sqla
from sqlalchemy.orm import Session

from classes import Card, CardArt
from classes.base import Base


ENGINE = sqla.create_engine("sqlite:///../assets/data/cards-data-v2.db", echo = True)


def setup_database():
  Base.metadata.create_all(ENGINE)


def update_cards(cards: list[Card]):
  with Session(ENGINE) as cnx:
    cnx.add_all(cards)
    cnx.commit()


def load_monsters():
  with Session(ENGINE) as cnx:
    out = cnx.execute(
      sqla.select(Card).where(Card.card_type == "monster")
    ).scalars().all()

  return out
