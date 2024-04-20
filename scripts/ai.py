import suptools as sup


def script():
  '''Create and train an instance of Ai.'''

  from ignis import Ai

  ai = Ai("Ai")

  sup.log(act = "initialising network...")
  ai.summon()

  sup.log(act = "loading data...")
  data = ai.materials()

  sup.log(act = "training network...")
  ai.activate(data)


if __name__ == "__main__":
  sup.run(script)
