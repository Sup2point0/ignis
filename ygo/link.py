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
  type_id = {}
  
  if "monster" in type:
    card = MonsterCard.from_json(data)
    type_id["monster_id"] = card.card_id
  else:
    card = SpellTrapCard.from_json(data)
    type_id["spelltrap_id"] = card.card_id

  arts = (
    CardArt(art_id = each["id"], **type_id)
    for each in data["card_images"]
  )

  return card, *arts


def bytes_to_image(data: bytes) -> Image:
  '''Convert `bytes` to a `PIL.Image` object.'''

  return Image.open(BytesIO(data))
