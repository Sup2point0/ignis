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
    attack: int,
    defense: int,
    pend: bool = False,
    *args, **kwargs
  ):
    super().__init__(*args, **kwargs)

    sup.init(self,
      kind = kind,
      race = race,
      attribute = attribute,
      level = level,
      attack = attack,
      defense = defense,
      pend = pend,
    )

  @ staticmethod
  def from_dict(data: dict) -> MonsterCard:
    '''Create a monster card with data from a `dict`.'''

    return Card.from_dict(data, MonsterCard,
      kind = data["frameType".split("_")[0]].lower(),
      race = data["race"].lower(),
      attribute = data["attribute"].upper(),
      level = data.get("level", data.get("linkval")),
      attack = data["atk"],
      defense = data.get("def", None),
      pend = ("pendulum" in data["frameType"].lower()),
    )
  
  def as_dict(self) -> dict:
    return {
      **super().as_dict(),
      "level": self.level,
      "attack": self.attack,
      "defense": self.defense,
    }
