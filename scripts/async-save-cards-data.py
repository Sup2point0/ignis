import suptools as sup


def script():
  '''
  Script for loading data from the local JSON file and saving it to the databse.
  '''

  import asyncio
  import json
  import random

  import ygo

  with open("../assets/data/cards-data.json", "r") as file:
    # data = json.load(file)
    data = random.choices(json.load(file), k = 20)
  
  asyncio.run(ygo.api.async_save_cards_art(data))


if __name__ == "__main__":
  sup.run(script)
