from __future__ import annotations

import suptools as sup
from .. import api


class Card:
  '''Represents any card with an unspecified type.'''

  def __init__(self,
    id: int,
    name: str,
    art: bytes,
  ):
    sup.init(id, name, art)

  @ staticmethod
  def from_dict(data: dict, cls = None, **kwargs) -> Card:
    '''Create a card using data from a `dict`.'''

    if cls is None:
      cls = Card
    
    return cls(
      id = data["id"],
      name = data["name"],
      art = api.get_card_art(data["card_images"]["image_url"]).raw,
      **kwargs
    )

  def as_dict(self) -> dict:
    '''Extract the `dict` representation of a card.'''

    return vars(self)
