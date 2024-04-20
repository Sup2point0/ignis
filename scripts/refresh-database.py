import suptools as sup


@ sup.vitals(view = True)
def script():
  '''
  Script for fetching and saving cards data from the YGOPRODECK API.
  '''

  import json

  import ygo

  sup.log(action = "fecthing data...")
  ygo.api.save_cards_data()

  sup.log(action = "loading JSON...")
  with open("../assets/data/cards-data.json", "r") as file:
    data = json.load(file)

  cards = [ygo.link.dict_to_card(each) for each in data]
  
  sup.log(action = "renewing database...")
  ygo.sql.refresh()
  
  sup.log(action = "updating database...")
  ygo.sql.update_monsters_data(cards)


if __name__ == "__main__":
  sup.run(script)
