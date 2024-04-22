from io import BytesIO

import requests
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


def url(card: dict) -> str:
  '''Find the URL on Yugipedia of a card, given its ID.'''
  
  password = card["id"]
  url = (
    "https://yugipedia.com/api.php?action=askargs"
    f"&conditions=Password::{password}&format=json"
  )

  load = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})
  
  data = load.json()["query"]
  found = data["results"]

  # find the closest match, which is most likely the shortest
  target = sorted(
    (
      key for key in found.keys()
      if key.casefold().startswith(card["name"].casefold())
    ),
    key = lambda card: len(card)
  )[0]
  out = found[target]

  return out["fullurl"]
