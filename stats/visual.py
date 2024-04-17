'''
...
'''

from collections import Counter

from matplotlib import pyplot as plt

import ygo


class Visual:
  '''...'''

  def __init__(self, property, **constraints):
    cards = ygo.sql.get_monsters_data()
    cards = (
      card[property] for card in cards
      if all(card[key] == val for key, val in constraints)
    )

    self.data = Counter(cards)
    self.x, self.y = zip(*self.data.items())

  def display(self):
    '''...'''

    self.figure, self.axes = plt.subplots()
    self.axes.bar(self.x, self.y)

    plt.show()
