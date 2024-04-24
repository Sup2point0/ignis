from io import BytesIO

from PIL import Image

import suptools as sup
from .classes import Card, MonsterCard


@ sup.vitals(catch = Exception)
def dict_to_card(data: dict) -> Card | MonsterCard:
  '''Extract data from a `dict` into a `Card` (or a subclass) object.'''

  type = data["type"].lower()
  
  if "monster" in type:
    return MonsterCard.from_dict(data)
  else:
    return Card.from_dict(data)


def bytes_to_image(data: bytes) -> Image:
  '''Convert `bytes` to a `PIL.Image` object.'''

  return Image.open(BytesIO(data))
