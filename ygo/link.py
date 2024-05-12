'''
Links parts of the `ygo` module together.
'''

from io import BytesIO
from typing import Iterable

from PIL import Image

import suptools as sup
from .classes import Card, MonsterCard, SpellTrapCard, CardArt


@ sup.vitals(catch = None)
def cards_and_art_from_json(data: dict) -> Iterable[Card | CardArt]:
  '''Extract `Card` (or subclass) and `CardArt` objects from API JSON data.'''

  type = data["type"].casefold()
  
  if "monster" in type:
    card = MonsterCard.from_json(data)
  else:
    card = SpellTrapCard.from_json(data)

  


def bytes_to_image(data: bytes) -> Image:
  '''Convert `bytes` to a `PIL.Image` object.'''

  return Image.open(BytesIO(data))
