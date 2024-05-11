'''
Handles interaction with the SQL database through SQLAlchemy.
'''

import os
import pathlib
from typing import Iterable, Callable

import sqlalchemy as sqla
from sqlalchemy.orm import Session

from .classes import Card, CardArt
from .classes.base import Base


ROUTE = "../assets/data/cards-data-v2.db"
ENGINE = sqla.create_engine(f"sqlite:///{ROUTE}", echo = True)


def refresh_database():
  '''Setup the database, overwriting an existing one if it exists.'''

  if pathlib.Path(ROUTE).exists():
    os.remove(ROUTE)

  Base.metadata.create_all(ENGINE, checkfirst = False)


def save(cards: list[Base]):
  with Session(ENGINE) as cnx:
    cnx.add_all(cards)
    cnx.commit()


def load(table: Base, constraints: list[Callable]) -> Iterable[Base]:
  with Session(ENGINE) as cnx:
    query = sqla.scalars(table)
    for constraint in constraints:
      query = query.where(constraint())
    
    out = cnx.execute(query)
    out = out.all()

  return out


def load_card_arts(constraints) -> Iterable[CardArt]:
  '''Load `CardArt` obejects from the database alongside the cards they represent.'''

  with Session(ENGINE) as cnx:
    query = sqla.scalars(CardArt).where(CardArt.card_id == Card.card_id)
    for constraint in constraints:
      query = query.where(constraint())
    
    out = cnx.execute(query)
    out = out.all()

  return out
