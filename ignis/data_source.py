'''
Implements the `DataSource` class for sourcing training data.
'''

import math
from typing import Iterable

import numpy as np
from tensorflow import keras

import ygo


class DataSource(keras.utils.Sequence):
  def __init__(self,
    data,  ### TODO FIXME
    art_ids: Iterable[int],
    labels,
    batch_size = 32,
    dimensions = (32, 32, 32),
    channel_count = 1,
    class_count = 10,
    shuffle = True,
  ):
    self.art_ids = art_ids
    self.labels = labels
    self.batch_size = batch_size
    self.dimensions = dimensions
    self.channel_count = channel_count
    self.class_count = class_count
    self.shuffle = shuffle
    
    self.indexes = np.arange(len(art_ids))

  def __len__(self):
    '''Find the number of batches per epoch.'''
    
    return math.floor(len(self.art_ids) / self.batch_size)

  def __getitem__(self, index):
    '''Generate a single batch of data.'''
  
    start = index * self.batch_size
    stop = (index+1) * self.batch_size
    indexes = self.indexes[start:stop]

    art_ids = [self.art_ids[i] for i in indexes]
    x, y = self.__data_generation(art_ids_temp)

    return x, y

  def on_epoch_end(self):
    '''Update indices after epochs.'''
    
    if self.shuffle:
        np.random.shuffle(self.indexes)

  def __data_generation(self, art_ids: Iterable[int]):
    # x: (n_samples, *dim, channel_count)
    images = np.empty((self.batch_size, *self.dim, self.channel_count))
    labels = np.empty((self.batch_size), dtype = int)

    for i, art_id in enumerate(art_ids):
        images[i,] = 0  ### TODO FIXME
        labels[i] = self.labels[ID]

    return x, keras.utils.to_categorical(labels, num_classes = self.class_count)
