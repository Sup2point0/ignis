'''
Implements the `Ignis` base class for Ignis to derive from.
'''

from tensorflow.keras import Model, layers


class Ignis:
  '''Base class for Ignis to derive from.'''

  def __init__(self,
    root,
    layers: list,
  ):
    '''Create an Ignis.'''

    self.summon_model(root, layers)

  def summon_model(self, root, layers):
    network = root
    
    for layer in layers:
      network = layer(network)

    self.model = Model(root, network)
