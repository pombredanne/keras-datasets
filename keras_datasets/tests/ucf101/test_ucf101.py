#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from keras_datasets.ucf101 import Ucf101
import os


class MyTest(TestCase):
    def test_download(self):
        instance = Ucf101()
        self.assertTrue(os.path.isdir(instance.path))
