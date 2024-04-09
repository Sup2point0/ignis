'''
Ai, the Ignis for predicting Monster Types and Attributes.
'''

from tensorflow.keras import Model, layers

from .ignis import Ignis
import ygo


class Ai(Ignis):
  '''Ai, the Ignis for predicting Monster Types and Attributes.'''

  def __init__(self):
    super().__init__()
