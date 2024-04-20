'''
...
'''

from collections import Counter

from matplotlib import pyplot as plt

import suptools as sup
import ygo


class Visual:
  '''...'''
  
  @ sup.vitals(view = True)
  def __init__(self, property, **constraints):
    '''...'''

    sup.log(action = "loading data...")
    cards = ygo.sql.load_monsters_data()

    sup.log(action = "filtering cards...")
    cards = (
      card[property] for card in cards
      if all(card[key] == val for key, val in constraints)
    )

    sup.log(action = "sorting cards...")
    data = Counter(cards)
    data = sorted(data.items(), key = (lambda card: card[1]))

    self.x, self.y = zip(*data)
    self.figure, self.axes = plt.subplots()
    self.axes.bar(self.x, self.y)

    plt.setp(self.axes.get_xticklabels(),
      rotation = 30, ha = "right", fontsize = 10,
    )

  def view(self):
    plt.show()
