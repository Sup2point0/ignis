from contextlib import closing
import sqlite3 as sqlite


ROUTE = "../assets/data/cards-data.db"


def query(name: str) -> str:
  '''Get a particular query stored in `ygo/queries/`.'''

  with open(f"../ygo/queries/{name}.sql") as file:
    text = file.read()

  return text


def refresh():
  with closing(sqlite.connect(ROUTE)) as ctx:
    with ctx:
      ctx.execute(query("refresh"))


def update_cards_data(cards: list):
  with closing(sqlite.connect(ROUTE)) as ctx:
    with ctx:
      ctx.executemany(query("update-monsters"), (card.as_json() for card in cards))
