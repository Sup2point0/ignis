from .classes import Card, MonsterCard


def json_to_card(data: dict) -> Card | MonsterCard:
    '''Extract data from JSON into a `Card` (or a subclass) object.'''

    type = data["type"].lower()
    
    try:
      if "monster" in type:
        return MonsterCard.from_dict(data)
      else:
        return Card.from_dict(data)
    except:
       return None 