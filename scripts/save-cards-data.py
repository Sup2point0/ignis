import suptools as sup


def script():
  import json

  import ygo
  
  with open("../assets/data/cards-data.json", "r") as file:
    data = json.load(file)[1100:2000]
    ygo.api.save_cards_data(data)


if __name__ == "__main__":
  sup.run(script)
