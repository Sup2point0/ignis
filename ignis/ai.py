'''
Ai, the Ignis for predicting Monster Types and Attributes.
'''

from tensorflow.keras import Model, layers

from .ignis import Ignis
import ygo


class Ai(Ignis):
  '''Ai, the Ignis for predicting Monster Types and Attributes.'''

  def __init__(self):
    super().__init__(
      root = layers.Input(shape = (100, 100, 3)),  ### FIXME
      layers = [
        layers.Conv2D(16, 3, activation = "relu"),
        layers.MaxPooling2D(2),
        layers.Conv2D(16, 3, activation = "relu"),
        layers.MaxPooling2D(2),
      ],
    )
