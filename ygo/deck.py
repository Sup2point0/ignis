'''
Handles loading decks from XML files exported from DuelingBook.
'''

import xml.etree.ElementTree as et
from collections import Counter


def load(data: str) -> dict:
  '''Load the names of the cards in a deck from an XML file.'''

  out = {}

  root = et.fromstring(data)
  out["deck"] = root.attrib["name"]

  for deck in root:
    cards = Counter(card.text for card in deck)
    out[deck.tag] = {
      "cards": dict(cards),
      "cards-total": cards.total(),
      "cards-unique": len(list(cards)),  ### NOTE can we find a more efficient method?
    }

  return out
