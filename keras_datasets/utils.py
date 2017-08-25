#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (unicode_literals,
                        absolute_import,
                        division,
                        print_function)

from keras_datasets import data_utils
import time
import datetime
import requests, threading
from enum import Enum
import csv
import numpy as np
from PIL import Image as pil_image


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
        raise NotImplementedError("Subclasses should implement this!")

    def __iter__(self):
        # Needed if we want to do something like:
        # for x, y in data_gen.flow(...):
        return self

    def __next__(self, *args, **kwargs):
        return self.next(*args, **kwargs)

    def _sample_decoder(self, path, *args, **kwargs):
        raise NotImplementedError("Subclasses should implement this!")

    def next(self, *args, **kwargs):
        # Maybe do a mother class with _flow_index and _sample reader
        with self.lock:
            index_array, current_index, current_batch_size = next(
                self.index_generator)

        # Open table of reference as an array of arrays.
        # table_ref = [["path1", class_a], ["path2", class_a] ...]
        table_ref = []
        with open(self.ref_table, 'r') as mfile:
            for row in csv.reader(mfile):
                if len(row) >= 2:
                    x, y = row
                    y = int(y)
                    table_ref.append((x,y))

            table_ref = table_ref[1:]  # Remove 1st line


        batch_x = []
        batch_y = []
        for i, j in enumerate(index_array):
            path = table_ref[j][0]
            batch_y.append(table_ref[j][1])
            batch_x.append(self._sample_decoder(path))  
            # Maybe add transorfmation options
            # Maybe save to h5py

        return batch_x, batch_y


def load_img(path, grayscale=False, target_size=None):
    """Loads an image into PIL format.

    # Arguments
        path: Path to image file
        grayscale: Boolean, whether to load the image as grayscale.
        target_size: Either `None` (default to original size)
            or tuple of ints `(img_height, img_width)`.

    # Returns
        A PIL Image instance.

    # Raises
        ImportError: if PIL is not available.
    """
    if pil_image is None:
        raise ImportError('Could not import PIL.Image. '
                          'The use of `array_to_img` requires PIL.')
    img = pil_image.open(path)
    if grayscale:
        if img.mode != 'L':
            img = img.convert('L')
    else:
        if img.mode != 'RGB':
            img = img.convert('RGB')
    if target_size:
        hw_tuple = (target_size[1], target_size[0])
        if img.size != hw_tuple:
            img = img.resize(hw_tuple)
    return img

def img_to_array(img):
    """Converts a PIL Image instance to a Numpy array.

    # Arguments
        img: PIL Image instance.

    # Returns
        A 3D Numpy array.

    # Raises
        ValueError: if invalid `img` is passed.
    """
    x = np.asarray(img, dtype='float32')
    if len(x.shape) == 2:
        x = x.reshape((x.shape[0], x.shape[1], 1))
    return x
