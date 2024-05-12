'''
Links parts of the `ygo` module together.
'''

from io import BytesIO
from typing import Iterable

from PIL import Image

import suptools as sup
from .classes import Card, MonsterCard, CardArt


@ sup.vitals(catch = Exception)
def cards_and_art_from_json(data: dict) -> Iterable[Card | MonsterCard | CardArt]:
  '''Extract `Card` (or subclass) and `CardArt` objects from API JSON data.'''

  type = data["type"].casefold()
  
  if "monster" in type:
    return MonsterCard.from_dict(data)
  else:
    return Card.from_dict(data)


def bytes_to_image(data: bytes) -> Image:
  '''Convert `bytes` to a `PIL.Image` object.'''

  return Image.open(BytesIO(data))
