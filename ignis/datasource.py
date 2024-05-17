'''
Implements the `DataSource` class for sourcing data from the database.
'''

import json
import math
import pathlib
from typing import Iterable

import numpy as np
from tensorflow import keras
import keras.utils
from matplotlib.image import imread
from skimage.transform import resize

import suptools as sup
import config
import ygo
from ygo import Card, CardArt


class DataSource(keras.utils.Sequence):
  '''Sources data from the database for training and testing the Ignis.'''

  SOURCE = pathlib.Path(config.ROOT, "assets/images/")
  FEATURES = {}

  def __init__(self,
    data: list[tuple[CardArt, Card]],
    feature: str,
    features: int,
    batchsize = 32,
    resize = (300, 300),
    shuffle = True,
  ):
    self.data = data
    self.feature = feature
    self.features = features

    self.points = len(data)
    self.indexes = np.arange(self.points)
    self.batchsize = batchsize
    self.batches = math.floor(self.points / batchsize)

    self.resize = resize
    self.shuffle = shuffle

  def __len__(self):
    return self.batches

  def __getitem__(self, index):
    '''Generate a single batch of data.'''
  
    start = index * self.batchsize
    stop = min(start + self.batchsize, self.points)
    indexes = self.indexes[start:stop]

    # x data
    arts = (
      self._try_load_(f"{row[0].art_id}.jpg")
      for row in self.data[start:stop]
      # for idx in indexes
      # for row in self.data[idx]
    )
    images = np.array([
      resize(each, self.resize)
      for each in arts if each is not False
    ])

    # y data
    features = np.array([
      self.FEATURES[self.feature][getattr(row[1], self.feature).casefold()]
      for row in self.data[start:stop]
    ])
    labels = keras.utils.to_categorical(features, num_classes = self.features)

    return images, labels

  def on_epoch_end(self):
    '''Update indices after epochs.'''
    
    if self.shuffle:
      np.random.shuffle(self.indexes)

  def _try_load_(self, filename: str) -> np.ndarray | bool:
    '''Try to load an image from local storage.
    
    If an error occurs, return `False` instead.
    '''

    try:
      return imread(self.SOURCE / filename)
    except:
      return False


with open(config.ROOT / "assets/data/ignis-features.json", "r") as file:
  DataSource.FEATURES = json.load(file)
