import urllib
from io import BytesIO
import urllib.parse

from PIL import Image

import suptools as sup
from .classes import Card, MonsterCard


@ sup.vitals(catch = None)
def dict_to_card(data: dict) -> Card | MonsterCard:
  '''Extract data from a `dict` into a `Card` (or a subclass) object.'''

  type = data["type"].lower()
  
  try:
    if "monster" in type:
      return MonsterCard.from_dict(data)
    else:
      return Card.from_dict(data)
  except:
    if True:
      print(data)
      raise


def bytes_to_image(data: bytes) -> Image:
  '''Convert `bytes` to a `PIL.Image` object.'''

  return Image.open(BytesIO(data))


def url(name) -> str:
  '''Format the URL on Yugipedia of a given card.'''

  sanitised = name.casefold().replace(" ", "_")
  return f"https://yugipedia.com/wiki/{sanitised}"
