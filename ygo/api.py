import asyncio
import json

import requests
import aiohttp
from tqdm import tqdm

import suptools as sup
from . import link, sql
from .classes import Card


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
  '''Save data from the YGOPRODECK API to a JSON file.'''

  with open("data/cards.json", "w") as file:
    sup.io.save_json(data, file)


async def async_load_card_art(ctx: aiohttp.ClientSession, card: Card, **kwargs):
  '''Asynchronously get and set the art for a card given its ID.'''

  url = f"https://images.ygoprodeck.com/images/cards_cropped/{card.id}.jpg"

  async with ctx.get(url, **kwargs) as response:
    card.art = await response.read()

  # sup.log(collected = card.name)


async def async_save_cards(data: dict) -> list[Card]:
  total = len(data)
  cards = [link.dict_to_card(each) for each in data]
  valid = len(cards)
  sup.log(action = f"loaded {valid}/{total} cards")

  sup.log(action = "collecting tasks...")
  async with aiohttp.ClientSession() as ctx:
    tasks = []

    for card in cards:
      task = asyncio.create_task(async_load_card_art(ctx, card))
      tasks.append(task)
    
    for card in tqdm(asyncio.as_completed(tasks), total = len(tasks)):
      await card
  
  sql.update_monsters_data(cards)
