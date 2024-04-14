from contextlib import closing
import sqlite3 as sqlite


ROUTE = "../assets/data/cards-data.db"


def query(name: str) -> str:
  '''Get a particular query stored in `ygo/queries/`.'''

  with open(f"../ygo/queries/{name}.sql", "r") as file:
    text = file.read()

  return text


def connect():
  return closing(sqlite.connect(ROUTE))


def refresh():
  with connect() as ctx:
    with ctx:
      ctx.executescript(query("refresh"))


def update_cards_data(cards: list):
  with connect() as ctx:
    with ctx:
      ctx.executemany(query("update-monsters"), (card.as_dict() for card in cards))


def get_monsters_data(**kwargs):
  q = query("get-monsters")

  if kwargs:
    q += "WHERE " + "\n".join(f"{key} = {val}" for key, val in kwargs.items())
  
  with connect() as ctx:
    out = ctx.execute()
    # out = out.fetchall()

  return out.fetchall()
