'''
Test that we can load the art for a card from the bytes stored in the database.
'''

import random
from io import BytesIO

from PIL import Image

import suptools as sup
import ygo


def test_load_art():
  card = random.choice(ygo.sql.load_monsters_data())
  img = Image.open(BytesIO(card["art"]))
  img.show()


if __name__ == "__main__":
  sup.run(test_load_art)
