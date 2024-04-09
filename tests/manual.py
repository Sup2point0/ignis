import suptools as sp

import ygo

with open("../assets/data/cards-data.json", "r+") as file:
  sp.io.restructure_json(file)

print("STATUS: DONE!")
