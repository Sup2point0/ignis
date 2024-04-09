from __future__ import annotations


class Card:
  '''Represents any card with an unspecified type.'''

  def __init__(self,
    id: int,
    card_name: str,
    image_filename: str,
  ):
    self.id = id
    self.card_name = card_name
    self.image_filename = image_filename

  @ staticmethod
  def from_json(data: dict) -> Card:
    '''Extract data from JSON into a `Card` object.'''
