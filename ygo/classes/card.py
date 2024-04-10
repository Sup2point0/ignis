from __future__ import annotations

from .. import api


class Card:
  '''Represents any card with an unspecified type.'''

  def __init__(self,
    id: int,
    name: str,
    art: bytes,
  ):
    self.id = id
    self.name = name
    self.art = art

  @ staticmethod
  def from_json(data: dict) -> Card:
    return Card(
      id = data["id"],
      name = data["name"],
      art = api.get_card_art(data["card_images"]["image_url"])
    )
