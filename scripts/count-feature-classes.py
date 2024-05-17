import suptools as sup


def script():
  '''Count the number of distinct classes for a particular card feature.'''

  import json

  import config
  import ygo

  data = ygo.sql.load(ygo.MonsterCard)
  features = set(card.race for card in data)

  with open(config.ROOT / "assets/data/ignis-classes.json", "r+") as file:
    data = json.load(file)
    data["race"] = {feature: i for i, feature in enumerate(features)}
    file.seek(0)
    json.dump(data, file, indent = 2)


if __name__ == "__main__":
  sup.run(script)
