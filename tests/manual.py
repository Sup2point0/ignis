import shutil

import requests
import suptools as sup

import ygo

import json
with open("../assets/data/cards-data.json", "r") as file:
  data = json.load(file)

  ygo.api.save_cards_data(data)

# with open("../assets/test.jpg", "wb") as file:
#   response = requests.get("https://images.ygoprodeck.com/images/cards_cropped/44256816.jpg", stream = True)

#   shutil.copyfileobj(response.raw, file)

#   del response

print("STATUS: DONE!")
