'''
Implements the `Ignis` base class for Ignis to derive from.
'''

# import tensorflow as tf
from tensorflow import keras
from keras import layers

import suptools as sup
import ygo


class Ignis:
  '''Base class for Ignis to derive from.'''

  class defaults:
    rate = 10 ** -6
    epochs = 3

  class presets:
    layers = {
      "sanitise": [
        layers.Resizing(200, 200, interpolation = "bilinear"),
        layers.Rescaling(1/255),
      ],
      "train": [
        layers.RandomFlip(mode = "horizontal")
      ],
    }

  def __init__(self, shard: str):
    '''Create an Ignis.'''

    self.shard = shard
    self.model = None

    self.path = f"../assets/models/{self.shard}"

  def summon(self,
    root: layers.Input,
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

  def activate(self, data, epochs = None):
    '''Train the network.'''

    if self.model is None:
      raise ValueError("network nonexistent!")

    self.model.compile(
      optimizer = keras.optimizers.RMSprop(learning_rate = self.rate),
      loss = "categorical_crossentropy",
      metrics = ["accuracy"],
    )

    self.model.fit(data,
      epochs = epochs or Ignis.defaults.epochs,
      verbose = 2,
      # validation_split = 0.1,
      shuffle = False,
    )

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
