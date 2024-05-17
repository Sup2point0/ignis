'''
Implements the `DataSource` class for sourcing data from the database.
'''

import math
from typing import Iterable

import numpy as np
from tensorflow import keras
import keras.utils
from skimage.io import imread
from skimage.transform import resize

import suptools as sup
import ygo
from ygo import Card, CardArt


class DataSource(keras.utils.Sequence):
  '''Sources data from the database for training and testing the Ignis.'''

  SOURCE = "../.assets/images/"

  def __init__(self,
    data: list[tuple[CardArt, Card]],
    feature: str,
    classes: int,
    batchsize = 32,
    resize = (300, 300),
    shuffle = True,
  ):
    self.data = data
    self.feature = feature
    self.classes = classes

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
    arts = [
      resize(
        imread(f"{self.ROUTE}{row[0].art_id}.jpg"),
        self.resize
      )
      for row in self.data[start:stop]
      # for idx in indexes
      # for row in self.data[idx]
    ])

    # y data
    features = np.array([
      getattr(row[1], self.feature)
      for row in self.data[start:stop]
    ])
    labels = keras.utils.to_categorical(features, num_classes = self.classes)

    return arts, labels

  def on_epoch_end(self):
    '''Update indices after epochs.'''
    
    if self.shuffle:
      np.random.shuffle(self.indexes)
