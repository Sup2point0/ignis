import suptools as sup


def script():
  '''Create and train an instance of Ai.'''

  import numpy as np

  import ygo
  from ignis import Ai
  from ignis import DataSource

  ai = Ai("Ai")
  ai.summon()
  ai.model.summary()

  data = ygo.sql.load_monster_arts()
  ds = DataSource(data, "attribute", 7)

  sup.log(act = "training network...")
  ai.activate(ds, epochs = 4)

  predict = ai.declare(np.array(data[-200:-1]))

  for i in range(-200, -1):
    sup.log(target = data[i])
    sup.log(predict = predict[i])


if __name__ == "__main__":
  sup.run(script)
