'''
Implements the `DataSource` class for sourcing data from the database.
'''

import math
from typing import Iterable

import numpy as np
from tensorflow import keras
import keras.utils

import suptools as sup
import ygo
from ygo.classes import Card, CardArt


class DataSource(keras.utils.Sequence):
  '''Sources cards data from the database.'''

  def __init__(self,
    data: list,  ### TODO FIXME
    art_ids: Iterable[int],
    labels,
    batchsize = 32,
    dimensions = (32, 32, 32),
    channels = 1,
    classes = 10,
    shuffle = True,
  ):
    sup.init(self,
      art_ids = art_ids,
      labels = labels,
      batchsize = batchsize,
      dimensions = dimensions,
      channels = channels,
      classes = classes,
      shuffle = shuffle,
    )
    
    self.indexes = np.arange(len(art_ids))

  def __len__(self):
    '''Find the number of batches per epoch.'''
    
    return math.floor(len(self.art_ids) / self.batchsize)

  def __getitem__(self, index):
    '''Generate a single batch of data.'''
  
    start = index * self.batchsize
    stop = (index+1) * self.batchsize
    indexes = self.indexes[start:stop]

    art_ids = [self.art_ids[i] for i in indexes]
    x, y = self.__data_generation(art_ids)

    return x, y

  def on_epoch_end(self):
    '''Update indices after epochs.'''
    
    if self.shuffle:
        np.random.shuffle(self.indexes)

  def __data_generation(self, art_ids: Iterable[int]):
    # x: (n_samples, *dim, channels)
    images = np.empty((self.batchsize, *self.dim, self.channels))
    labels = np.empty((self.batchsize), dtype = int)

    for i, art_id in enumerate(art_ids):
        images[i,] = 0  ### TODO FIXME
        labels[i] = self.labels[art_id]

    return images, keras.utils.to_categorical(labels, num_classes = self.classes)
