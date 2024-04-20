from __future__ import annotations

import suptools as sup
from .. import api


class Card:
  '''Represents any card with an unspecified type.'''

  def __init__(self,
    id: int,
    name: str,
    type: str,
    art: bytes = None,
  ):
    sup.init(self, id = id, name = name, type = type, art = art)

  @ staticmethod
  def _sanitise_type_(text: str) -> str:
    text = text.casefold()

    if "monster" in text:
      return "monster"
    if "spell" in text:
      return "spell"
    if "trap" in text:
      return "trap"

  @ staticmethod
  def from_dict(data: dict, cls = None, **kwargs) -> Card:
    '''Create a card using data from a `dict`.'''

    if cls is None:
      cls = Card
    
    return cls(
      id = data["id"],
      name = data["name"],
      type = Card._sanitise_type_(data["type"]),
      **kwargs
    )

  def as_dict(self) -> dict:
    '''Extract the `dict` representation of a card.'''

    return vars(self)
