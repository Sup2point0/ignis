from __future__ import annotations

import suptools as sup
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
    pend: bool = False,
    *args, **kwargs
  ):
    super().__init__(*args, **kwargs)

    sup.init(self,
      kind = kind,
      race = race,
      attribute = attribute,
      level = level,
      atks = atks,
      defs = defs,
      pend = pend,
    )

  @ staticmethod
  def from_dict(data: dict) -> MonsterCard:
    '''Create a monster card with data from a `dict`.'''

    return Card.from_dict(data, MonsterCard,
      kind = data["frameType"].lower(),
      race = data["race"].lower(),
      attribute = data["attribute"].upper(),
      level = data["level"],
      atks = data["atk"],
      defs = data["def"],
      pend = ("pendulum" in data["frameType"].lower()),
    )
