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
    ctx.execute(query("refresh"))
