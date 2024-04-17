import json

import requests

from . import link, sql


def get_cards_data(**kwargs) -> dict:
  request = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
  if kwargs:
    request += "?" + "&".join(f"{key}={val}" for key, val in kwargs.items())

  response = requests.get(request)
  status = response.status_code

  if status == 200:
    return response.json()
  else:
    raise Exception(f"status {status}")


def get_card_art(id: int) -> requests.Response:
  '''Get the art for a card given its ID.'''

  return requests.get(f"https://images.ygoprodeck.com/images/cards_cropped/{id}.jpg")


def save_cards_data(data: dict):
  cards = [link.json_to_card(each) for each in data]
  cards = [card for card in cards if card]
  sql.update_monsters_data(cards)


def update_cards_data():
  data = get_cards_data()
  save_cards_data(data)
