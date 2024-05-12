import suptools as sup


def script():
  '''
  Load data from the local JSON file and save it to the database.
  '''

  import json
  import random

  import ygo

  with open("../assets/data/cards-data.json", "r") as file:
    data = json.load(file)
    # data = random.choices(json.load(file), k = 20)
  
  load = (ygo.link.cards_and_art_from_json(card) for card in data)
  assets = (asset for card in load for asset in card)
  ygo.sql.save(assets)


if __name__ == "__main__":
  sup.run(script)
