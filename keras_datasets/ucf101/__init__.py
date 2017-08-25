#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (unicode_literals,
                        absolute_import,
                        division,
                        print_function)

import os, sys

from keras_datasets import utils


class Ucf101(utils.Iterator):
    """Loads the UCF101 dataset in ~/.keras_datasets/datasets/ucf101.

    # Arguments
        none: blabla

    # Returns
        Well... It's a class... You know...
    """

    def __init__(self):
        self.url = "http://www.vision.caltech.edu/Image_Datasets/Caltech101/101_ObjectCategories.tar.gz"
        self.name = 'ucf101'
        self._download()
        self.path = os.path.expanduser(os.path.join('~',
                                                    '.keras_datasets',
                                                    self.name))
        super(Ucf101, self).__init__(n_samples=1000, batch_size=10)

    def _sample_reader(index):
        """Reads an image corresponding to a given index"""