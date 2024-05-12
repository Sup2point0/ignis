'''
Handles interaction with the YGOPRODECK and Yugipedia APIs.
'''

import asyncio
import json

import requests
import aiohttp
import fuzzywuzzy.process
from tqdm import tqdm

import suptools as sup
from . import sql
from .classes import Card


LOG = "../assets/data/fetch-log.json"


def fetch_cards_data(**kwargs) -> dict:
  with open(LOG, "r") as file:
    log = json.load(file)
  
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
  '''Save response from the YGOPRODECK API to a JSON file.'''

  with open("data/cards.json", "w") as file:
    sup.io.save_json(data, file)


async def async_fetch_card_art(ctx: aiohttp.ClientSession, card: Card, **kwargs):
  '''Asynchronously get and set the art for a card given its ID.'''

  url = f"https://images.ygoprodeck.com/images/cards_cropped/{card.id}.jpg"

  async with ctx.get(url, **kwargs) as response:
    card.art = await response.read()

  # sup.log(collected = card.name)


def fetch_card_url(card: dict) -> str:
  '''Find the URL on Yugipedia of a card, given its ID.'''
  
  password = card["id"]
  url = (
    "https://yugipedia.com/api.php?action=askargs"
    f"&conditions=Password::{password}"
    "]][[Category:Duel%20Monsters%20cards&format=json"
  )

  load = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})
  found = load.json()["query"]["results"]

  target = fuzzywuzzy.process.extract(card["name"], found.keys(), limit = 1)
  out = found[target[0][0]]

  return out["fullurl"]


async def async_save_cards(data: dict) -> list[Card]:
  total = len(data)
  cards = [link.dict_to_card(each) for each in data]
  valid = len(cards)
  sup.log(action = f"loaded {valid}/{total} cards")

  sup.log(action = "collecting tasks...")
  async with aiohttp.ClientSession() as ctx:
    tasks = []

    for card in cards:
      task = asyncio.create_task(async_fetch_card_art(ctx, card))
      tasks.append(task)
    
    for card in tqdm(asyncio.as_completed(tasks), total = len(tasks)):
      await card
  
  sql.update_monsters_data(cards)
