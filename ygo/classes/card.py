from __future__ import annotations

import suptools as sup
from .. import api


class Card:
  '''Represents any card with an unspecified type.'''

  def __init__(self,
    id: int,
    name: str,
    art: bytes,
    type: str,
  ):
    sup.init(self, id = id, name = name, art = art, type = type)

  @ staticmethod
  def _sanitise_type_(text: str) -> str:
    text = text.casefold()

    def check(text, type):
      if type in text:
        return type

    check(text, "monster")
    check(text, "spell")
    check(text, "trap")

  @ staticmethod
  def from_dict(data: dict, cls = None, **kwargs) -> Card:
    '''Create a card using data from a `dict`.'''

    if cls is None:
      cls = Card
    
    return cls(
      id = data["id"],
      name = data["name"],
      art = api.get_card_art(data["card_images"][0]["image_url"]).content,
      type = Card._sanitise_type_(data["type"]),
      **kwargs
    )

  def as_dict(self) -> dict:
    '''Extract the `dict` representation of a card.'''

    return vars(self)
