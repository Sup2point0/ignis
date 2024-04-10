from __future__ import annotations

from . import card


Card = card.Card


class MonsterCard(Card):
  '''Represents a monster card.'''

  def __init__(self,
    kind: str,
    race: str,
    attribute: str,
    level: int,
    atks: int,
    defs: int,
    pend: bool,
    *args, **kwargs
  ):
    super().__init__(*args, **kwargs)

    sp.init(self, kind, race, attribute, level, atks, defs, pend)

  @ staticmethod
  def from_dict(data: dict) -> MonsterCard:
    '''Create a monster card with data from a `dict`.'''

    return Card.from_dict(data, MonsterCard,
      race = data["race"].lower(),
      attribute = data["attribute"].upper(),
    )

  def as_dict(self) -> dict:
    '''Extract the `dict` representation of a monster card.'''

    return sp.to_dict(self)
