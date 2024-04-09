import json

import requests

import suptools as sp


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


def save_cards_data(data: dict):
  with open("../assets/data/data.json", "r+") as file:
    existing = json.load(file)
    existing.update(data)
    sp.io.overwrite(file, json.dumps(existing))


def save_cards_images(data: dict):
  pass


def update_cards_data():
  data = get_cards_data()
  save_cards_data(data)
