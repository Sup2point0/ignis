'''
Handles interaction with the SQL database.
'''

import shutil
import sqlite3 as sqlite
from contextlib import closing
from io import BytesIO

import suptools as sup
from . import link
from .classes import Card, MonsterCard


ROUTE = "../assets/data/cards-data.db"


def query(name: str) -> str:
  '''Get a particular query stored in `ygo/queries/`.'''

  with open(f"../ygo/queries/{name}.sql", "r") as file:
    text = file.read()

  return text


def _connect_():
  '''Create a connection to the database.'''

  connection = sqlite.connect(ROUTE)
  connection.row_factory = sqlite.Row
  return closing(connection)


def refresh():
  '''Delete all cards in the database.'''

  with _connect_() as ctx:
    with ctx:
      ctx.executescript(query("refresh"))


def update_monsters_data(cards: list[Card]):
  monsters = (card.as_dict() for card in cards if isinstance(card, MonsterCard))
  
  with _connect_() as ctx:
    with ctx:
      ctx.executemany(query("update-monsters"), monsters)


def load_monsters_data(constraints: str = None) -> list:
  '''Load monsters from the database with `constraints`.'''

  q = query("get-monsters")

  if constraints:
    q += "WHERE " + constraints
 
  with _connect_() as ctx:
    out = ctx.execute(q)
    out = out.fetchall()

  return out


def extract_cards_art(data: list):
  '''Extract art for cards from given data to `assets/images`.'''

  for card in data:
    with open(f"../assets/images/{card['id']}.jpg", "wb") as file:
      shutil.copyfileobj(BytesIO(card["art"]), file)
      sup.log(act = "saved" + card["name"])
