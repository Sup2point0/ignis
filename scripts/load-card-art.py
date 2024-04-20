import suptools as sup


def script():
  '''Load art for a card from the database and save it to a file.'''

  import random
  import shutil

  import ygo

  cards = ygo.sql.get_monsters_data(attribute = "DARK")
  card = random.choice(cards)
  art = card["art"]
  path = f"../assets/images/{card['name']}.jpg"

  with open(path, "wb+") as file:
    file.write(art)


if __name__ == "__main__":
  sup.run(script)
