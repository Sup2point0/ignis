from .classes import Card, MonsterCard


def dict_to_card(data: dict) -> Card | MonsterCard:
  '''Extract data from a `dict` into a `Card` (or a subclass) object.'''

  type = data["type"].lower()
  
  try:
    if "monster" in type:
      return MonsterCard.from_dict(data)
    else:
      return Card.from_dict(data)
  except Exception as e:
    raise e
    return None
