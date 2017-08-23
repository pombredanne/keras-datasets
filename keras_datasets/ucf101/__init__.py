#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import utils
# from .. import data_utils
# import os


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
        super(Ucf101, self).__init__(n_samples=1000, batch_size=10)

    def _sample_reader(index):
        """Reads an image corresponding to a given index"""
