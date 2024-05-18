import suptools as sup


def script():
  '''Create and train an instance of Ai.'''

  import ygo
  from ignis import Ai
  from ignis import DataSource

  ai = Ai("Ai")
  ai.summon()

  data = ygo.sql.load_monster_arts()
  ds = DataSource(data, "attribute", 7)

  sup.log(act = "training network...")
  ai.activate(ds)


if __name__ == "__main__":
  sup.run(script)
