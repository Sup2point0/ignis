import suptools as sup


def script():
  '''Create and train an instance of Ai.'''

  from ignis import Ai

  ai = Ai("Ai")

  sup.log(act = "initialising network...")
  ai.summon()

  data = ai.materials()
  sup.log(data = data)
  # ai.activate(data)


if __name__ == "__main__":
  sup.run(script)
