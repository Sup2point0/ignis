'''
Implements the `Ignis` base class for Ignis to derive from.
'''

from tensorflow.keras import Model, layers, optimizers


class Ignis:
  '''Base class for Ignis to derive from.'''

  class defaults:
    rate = 10 ** -6
    epochs = 12

  def __init__(self,
    root,
    layers: list,
    rate: float = None,
    epochs: int = None,
  ):
    '''Create an Ignis.'''

    self.rate = learn_rate or Ignis.defaults.rate

    self.summon(root, layers)

  def summon(self, root, layers):
    '''Initialise the network.'''
    
    network = root
    
    for layer in layers:
      network = layer(network)

    self.model = Model(root, network)

  def activate(self, data):
    '''Train the network.'''

    if self.model is None:
      raise ValueError("network nonexistent!")

    self.model.compile(
      loss = "categorical_crossentropy",
      optimizer = optimizers.Adam(learning_rate = self.rate),
    )

    self.model.fit_generator(
      data,
      epochs = self.epochs
    )

  def declare(self, data):
    '''Use the network on given data.'''

    raise NotImplementedError()
