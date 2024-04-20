import suptools as sup


def script():
  import asyncio
  import json
  import random

  import ygo

  with open("../assets/data/cards-data.json", "r") as file:
    # data = json.load(file)
    data = random.choices(json.load(file), k = 200)
  
  asyncio.run(ygo.api.async_save_cards_art(data))


if __name__ == "__main__":
  sup.run(script)
