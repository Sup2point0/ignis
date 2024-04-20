import suptools as sup


def script():
  '''Load art for a card from the database and save it to a file.'''

  import random
  import shutil

  import ygo

  query = '''attribute = "FIRE"'''
  cards = ygo.sql.load_monsters_data(query)
  card = random.choice(cards)
  art = card["art"]
  path = f"../assets/images/{card['name']}.jpg"

  with open(path, "wb+") as file:
    file.write(art)


if __name__ == "__main__":
  sup.run(script)
