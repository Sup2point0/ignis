import suptools as sup


def script():
  '''
  Load data from the local JSON file and save it to the database.
  '''

  import json
  import random

  import ygo

  with open("../assets/data/cards-data.json", "r") as file:
    # data = json.load(file)
    data = random.choices(json.load(file), k = 20)
  
  cards = (ygo.Card.from_dict(card) for card in data)
  ygo.sql.setup_database()
  ygo.sql.update_cards(cards)


if __name__ == "__main__":
  sup.run(script)
