'''
Handles interaction with the SQL database through SQLAlchemy.
'''

from typing import Callable

import sqlalchemy as sqla
from sqlalchemy.orm import Session

from .classes import Card, CardArt
from .classes.base import Base


ENGINE = sqla.create_engine("sqlite:///../assets/data/cards-data-v2.db", echo = True)


def setup_database():
  Base.metadata.create_all(ENGINE)


def update_cards(cards: list[Card]):
  with Session(ENGINE) as cnx:
    cnx.add_all(cards)
    cnx.commit()


def load_cards(constraints: list[Callable]):
  with Session(ENGINE) as cnx:
    query = sqla.scalars(Card)
    for constraint in constraints:
      query = query.where(constraint())
    
    out = cnx.execute(query)
    out = out.all()

  return out
