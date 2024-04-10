from ..classes import Card


class MonsterCard(Card):
  '''Represents a monster card.'''

  def __init__(self,
    type: str,
    attribute: str,
    *args, **kwargs
  ):
    super().__init__(*args, **kwargs)

    self.type = type
    self.attribute = attribute
