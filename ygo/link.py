from .classes import Card, MonsterCard


def json_to_card(data: dict) -> Card:
    '''Extract data from JSON into a `Card` object.'''

    type = data["type"].lower()
    if "monster" in type:
      return MonsterCard.from_json(data)
    else:
      return Card.from_json(data)
