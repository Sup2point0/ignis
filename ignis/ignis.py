'''
Implements the `Ignis` base class for Ignis to derive from.
'''

from tensorflow import keras

import suptools as sup


class Ignis:
  '''Base class for Ignis to derive from.'''

  class defaults:
    rate = 10 ** -6
    epochs = 12

  def __init__(self, shard: str):
    '''Create an Ignis.'''

    self.shard = shard
    self.model = None

    self.path = f"../assets/models/{self.shard}"

  def summon(self,
    root: keras.layers.Input,
    layers: list,
    epochs: int = None,
    rate: float = None,
  ):
    '''Create a network.'''
    
    network = root
    
    for layer in layers:
      network = layer(network)

    self.model = keras.Model(root, network)
    
    self.rate = rate or Ignis.defaults.rate
    self.epochs = epochs or Ignis.defaults.epochs

  def activate(self, data):
    '''Train the network.'''

    if self.model is None:
      raise ValueError("network nonexistent!")

    self.model.compile(
      loss = "categorical_crossentropy",
      optimizer = keras.optimizers.RMSprop(lr = self.rate),
      metrics = ["acc"],
    )

    self.model.fit_generator(data, epochs = self.epochs)   ### FIXME

  def save(self):
    '''Save the model to local files.'''

    if self.model is None:
      raise ValueError("network nonexistent!")

    with open(self.path + ".json", "w") as file:
      sup.io.overwrite(file, self.mode.to_json())

    self.model.save_weights(self.path + ".h5")

  def draw(self):
    '''Load the model from local files.'''

    with open(self.path + ".json", "r") as file:
      self.model = keras.models.model_from_json(file.read())
      self.model.load_weights(self.path + ".h5")

  def declare(self, data):
    '''Use the network on given data.'''

    raise NotImplementedError()
