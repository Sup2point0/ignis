'''
Tests for fetching data from APIs.
'''

import suptools as sup
import ygo


def test_get_url():
  '''Test that we can find a card's URL on Yugipedia.'''

  card = {"name": "Blue-Eyes White Dragon", "id": 89631139}
  assert ygo.api.fetch_card_url(card) == "https://yugipedia.com/wiki/Blue-Eyes_White_Dragon"
