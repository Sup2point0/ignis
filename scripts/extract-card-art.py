import suptools as sup


def script():
  '''
  ...
  '''

  import ygo


  data = ygo.sql.load_monsters_data()
  ygo.sql.extract_cards_art(data)


if __name__ == "__main__":
  sup.run(script)
