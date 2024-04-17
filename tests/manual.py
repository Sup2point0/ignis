import shutil
from io import BytesIO

from PIL import Image
import requests
import suptools as sup

import ygo

# import json
# with open("../assets/data/cards-data.json", "r") as file:
#   data = json.load(file)[:1]

#   ygo.api.save_cards_data(data)

with open("../assets/test.jpg", "wb") as file:
  rows = ygo.sql.get_monsters_data()
  img = Image.open(BytesIO(rows[0][2]))
  img.show()

#   response = requests.get("https://images.ygoprodeck.com/images/cards_cropped/44256816.jpg", stream = True)

#   shutil.copyfileobj(response.raw, file)

#   del response

print("STATUS: DONE!")
