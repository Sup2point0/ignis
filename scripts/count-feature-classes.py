import suptools as sup


def script():
  '''Count the number of distinct classes for a particular card feature.'''

  import ygo

  data = ygo.sql.load(ygo.MonsterCard)

  sup.log(race = len(set(card.race for card in data)))


if __name__ == "__main__":
  sup.run(script)
