from ..classes import Card


class MonsterCard(Card):
  '''Represents a monster card.'''

  def __init__(self,
    race: str,
    attribute: str,
    *args, **kwargs
  ):
    super().__init__(*args, **kwargs)

    self.type = type
    self.attribute = attribute

  @ staticmethod
  def from_dict(data: dict) -> MonsterCard:
    '''Create a monster card with data from a `dict`.'''

    return Card.from_dict(data, MonsterCard,
      race = data["race"].lower(),
      attribute = data["attribute"].upper(),
    )
