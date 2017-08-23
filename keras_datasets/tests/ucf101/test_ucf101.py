#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

import os
from keras_datasets.ucf101 import Ucf101



class MyTest(TestCase):
    def test_download(self):
        instance = Ucf101()
        self.assertTrue(instance)
