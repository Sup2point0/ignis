'''
Handles interaction with the SQL database through SQLAlchemy.
'''

import os
import pathlib
from typing import Iterable, Callable

import sqlalchemy as sqla
from sqlalchemy.orm import Session

from config import ROOT
from .classes import Card, MonsterCard, CardArt


SOURCE = pathlib.Path(ROOT, "assets/data/cards-data-v2.db")
ENGINE = sqla.create_engine(f"sqlite:///{SOURCE}", echo = False)


def refresh_database():
  '''Setup the database, overwriting an existing one if it exists.'''

  if pathlib.Path(SOURCE).exists():
    os.remove(SOURCE)

  Card.metadata.create_all(ENGINE, checkfirst = False)


def save(cards: Iterable[Card]):
  with Session(ENGINE) as cnx:
    cnx.add_all(cards)
    cnx.commit()


def load(table: Card, constraints: Iterable[Callable] = []) -> Iterable[Card]:
  '''Load rows from a `table` with `constraints`.'''

  with Session(ENGINE) as cnx:
    query = sqla.select(table)
    for constraint in constraints:
      query = query.where(constraint)
    
    out = cnx.scalars(query)
    out = out.all()

  return out


def load_monster_arts(constraints: Iterable[Callable] = []) -> Iterable[CardArt]:
  '''Load `CardArt` objects from the database alongside the `MonsterCard`s they represent.'''

  with Session(ENGINE) as cnx:
    query = (
      sqla.select(CardArt, MonsterCard)
      .join(CardArt, CardArt.monster_id == MonsterCard.card_id)
    )
    
    for constraint in constraints:
      query = query.where(constraint)
    
    out = cnx.execute(query)
    out = out.all()

  return out
