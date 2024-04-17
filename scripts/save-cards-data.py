from scripts import Script


def script():
  import json

  import ygo
  
  with open("../assets/data/cards-data.json", "r") as file:
    data = json.load(file)[:42]

    ygo.api.save_cards_data(data)


if __name__ == "__main__":
  Script(script)
