from sqlalchemy.orm import DeclarativeBase


class Card(DeclarativeBase):
  '''Base class for other card tables to derive from.'''

  @ staticmethod
  def sanitise_type(text: str) -> str:
    text = text.casefold()

    if "monster" in text:
      return "monster"
    if "spell" in text:
      return "spell"
    if "trap" in text:
      return "trap"
    
    return "UNKNOWN"
