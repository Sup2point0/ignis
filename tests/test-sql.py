'''
Tests for loading data from local files.
'''

import random
from io import BytesIO

from PIL import Image

import suptools as sup
import ygo


def test_load_monster_cards():
  data = ygo.sql.load(ygo.MonsterCard)[:20]
  assert len(data) == 20
  assert all(isinstance(each, ygo.MonsterCard) for each in data)


def test_load_monster_arts():
  data = ygo.sql.load_monster_arts()[:20]
  assert len(data) == 20
  assert all(isinstance(each[0], ygo.CardArt) for each in data)
  assert all(isinstance(each[1], ygo.MonsterCard) for each in data)

  data = ygo.sql.load_monster_arts([ygo.MonsterCard.attribute == "DARK"])[:20]
  assert all(isinstance(each[0], ygo.CardArt) for each in data)
  assert all(isinstance(each[1], ygo.MonsterCard) for each in data)
  assert all(each[1].attribute == "DARK" for each in data)


def test_load_multiple_arts():
  data = ygo.sql.load_monster_arts([ygo.MonsterCard.card_id == 46986414])
  assert len(data) > 1


if __name__ == "__main__":
  sup.run(test_load_monster_cards)
