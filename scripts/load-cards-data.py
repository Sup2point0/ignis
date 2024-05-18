import suptools as sup


def script():
  '''Load cards data from the database.'''

  import ygo
  from random import choices

  data = ygo.sql.load_monster_arts([ygo.MonsterCard.attribute == "DARK"])

  for row in data:
    sup.log(row = row)


if __name__ == "__main__":
  sup.run(script)
