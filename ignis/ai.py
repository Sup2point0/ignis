'''
Ai, the Ignis for predicting Monster Types and Attributes.
'''

from keras import layers

from .ignis import Ignis


class Ai(Ignis):
  '''Ai, the Ignis for predicting Monster Types and Attributes.'''

  def summon(self):
    super().summon(
      root = layers.Input(shape = (600, 600, 3)),
      layers = [
        # *Ignis.presets.layers["sanitise"],
        *Ignis.presets.layers["train"],
        layers.Conv2D(16, 3, activation = "relu"),
        layers.MaxPooling2D(2),
        layers.Conv2D(32, 3, activation = "relu"),
        layers.MaxPooling2D(2),
        layers.Conv2D(64, 3, activation = "relu"),
        layers.MaxPooling2D(2),
        layers.Flatten(),
        layers.Dense(7, activation = "softmax"),
      ],
    )
