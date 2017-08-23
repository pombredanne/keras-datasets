#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (unicode_literals,
                        absolute_import,
                        division,
                        print_function)

import time, datetime
import requests, threading

import numpy as np
from enum import Enum

from keras_datasets import data_utils


class Compression(Enum):
    NONE = 1
    GZIP = 2
    ZLIB = 3


class Subset(Enum):
    TRAIN = 1
    TEST = 2
    VALIDATION = 3


compression_suffix = {
    Compression.NONE: '',
    Compression.GZIP: 'gzip',
    Compression.ZLIB: 'zlib'
}


subset_suffix = {
    Subset.TRAIN: 'train',
    Subset.TEST: 'test',
    Subset.VALIDATION: 'validation'
}


class Iterator(object):
    """Abstract base class for image data iterators.

    # Arguments
        batch_size: Integer, size of a batch.
        shuffle: Boolean, whether to shuffle the data between epochs.
        seed: Random seeding for data shuffling.
    """

    def __init__(self, n_samples, batch_size, shuffle=True, seed=None):
        self.n_samples = n_samples
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.batch_index = 0
        self.total_batches_seen = 0
        self.lock = threading.Lock()
        self.index_generator = self._flow_index(n_samples,
                                                batch_size,
                                                shuffle,
                                                seed)

    def reset(self):
        self.batch_index = 0

    def _flow_index(self, n, batch_size=32, shuffle=False, seed=None):
        """Ensure self.batch_index is 0, then produces batches of indices.

        # Yields:
            (np.array with indexes,
            current index in array of indexes,
            current batch_size)

        """
        self.reset()
        while 1:
            # Change seed at each epoch
            if seed is not None:
                np.random.seed(seed + self.total_batches_seen)

            # Maybe reset index array (random or not)
            if self.batch_index == 0:
                index_array = np.arange(n)
                if shuffle:
                    index_array = np.random.permutation(n)

            # Compute next batch size
            current_index = (self.batch_index * batch_size) % n
            if n > current_index + batch_size:
                current_batch_size = batch_size
                self.batch_index += 1
            else:  # Last batch of epoch
                current_batch_size = n - current_index
                self.batch_index = 0
            self.total_batches_seen += 1

            yield (
                index_array[current_index: current_index + current_batch_size],
                current_index,
                current_batch_size)

    def _download(self):
        # Download the dataset
        data_utils.get_file(self.name, self.url)

    def __iter__(self):
        # Needed if we want to do something like:
        # for x, y in data_gen.flow(...):
        return self

    def __next__(self, *args, **kwargs):
        return self.next(*args, **kwargs)

    def _sample_reader(self, index, *args, **kwargs):
        raise NotImplementedError("Subclasses should implement this!")

    def next(self, *args, **kwargs):
        # Maybe do a mother class with _flow_index and _sample reader
        raise NotImplementedError("Subclasses should implement this!")
