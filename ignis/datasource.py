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
# from matplotlib.image import imread
from skimage.io import imread
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
    batches: int = None,
    batchsize = 32,
    resize = (600, 600),
    shuffle = True,
    **kwargs,
  ):
    super().__init__(**kwargs)

    self.data = data
    self.feature = feature
    self.features = features

    self.points = len(data)
    self.indexes = np.arange(self.points)
    if batches:
      self.batches = batches
      self.batchsize = math.floor(self.points / self.batches)
    else:
      self.batchsize = batchsize
      self.batches = math.floor(self.points / batchsize)

    self.resize = resize
    self.shuffle = shuffle

  def __len__(self):
    return self.batches

  @ sup.vitals(view = True)
  def __getitem__(self, index):
    '''Generate a single batch of data.'''
  
    start = index * self.batchsize
    stop = min(start + self.batchsize, self.points)
    indexes = self.indexes[start:stop]

    # x data
    self.failed = set()
    arts = (
      self._try_load_(i, f"{row[0].art_id}.jpg")
      for i, row in enumerate(self.data[start:stop])
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
      for i, row in enumerate(self.data[start:stop])
      if i not in self.failed
    ])
    labels = keras.utils.to_categorical(features, num_classes = self.features)

    sup.log(index = f"{index} - {start}~{stop}")
    return images, labels

  def on_epoch_end(self):
    '''Update indices after epochs.'''
    
    if self.shuffle:
      np.random.shuffle(self.indexes)

  @ sup.vitals(view = True)
  def _try_load_(self, index: int, filename: str) -> np.ndarray | bool:
    '''Try to load an image from local storage.
    
    If an error occurs, return `False` instead.
    '''

    try:
      return imread(self.SOURCE / filename)
    except:
      self.failed.add(index)
      return False


with open(config.ROOT / "assets/data/ignis-features.json", "r") as file:
  DataSource.FEATURES = json.load(file)
