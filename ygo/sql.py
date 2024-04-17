from contextlib import closing
import sqlite3 as sqlite

from . import link
from .classes import Card, MonsterCard


ROUTE = "../assets/data/cards-data.db"


def query(name: str) -> str:
  '''Get a particular query stored in `ygo/queries/`.'''

  with open(f"../ygo/queries/{name}.sql", "r") as file:
    text = file.read()

  return text


def connect():
  connection = sqlite.connect(ROUTE)
  connection.row_factory = sqlite.Row
  return closing(connection)


def refresh():
  with connect() as ctx:
    with ctx:
      ctx.executescript(query("refresh"))


def update_monsters_data(cards: list[Card]):
  monsters = (card.as_dict() for card in cards if isinstance(card, MonsterCard))
  
  with connect() as ctx:
    with ctx:
      ctx.executemany(query("update-monsters"), monsters)


def get_monsters_data(**kwargs) -> list:
  q = query("get-monsters")

  if kwargs:
    q += "WHERE " + "\n".join(f"{key} = {val}" for key, val in kwargs.items())
  
  with connect() as ctx:
    out = ctx.execute(q)
    out = out.fetchall()

  return out
