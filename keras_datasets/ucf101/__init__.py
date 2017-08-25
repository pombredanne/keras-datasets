#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (unicode_literals,
                        absolute_import,
                        division,
                        print_function)


import csv
import os
import six

from keras_datasets import data_utils
from keras_datasets import utils


class Ucf101(utils.Iterator):
    """Loads the UCF101 dataset in ~/.keras_datasets/datasets/ucf101.

    # Arguments
        none: blabla

    # Returns
        Well... It's a class... You know...
    """

    def __init__(self):
        self.name = 'Caltech101'
        self.dir = self._download()
        self.ref_table = self.generate_reference_table()
        super(Ucf101, self).__init__(n_samples=1000, batch_size=10)

    def _download(self):
        """Download and untar images and anotations
        """
        url1 = "http://www.vision.caltech.edu/Image_Datasets/Caltech101/" \
               "101_ObjectCategories.tar.gz"
        url2 = "http://www.vision.caltech.edu/Image_Datasets/Caltech101/" \
               "Annotations.tar"

        # Download and extract desired files
        mfile = data_utils.get_file(url1, fdir='caltech101', extract=True)
        data_utils.get_file(url2, fdir='caltech101', extract=True)

        mdir = os.path.dirname(mfile)
        return mdir

    def generate_reference_table(self):
        """Generate a CSV with columns: File_path, Label1, Label2, ...
        """
        # Read classes names
        data_dir = os.path.join(self.dir, '101_ObjectCategories')
        classes = []
        for subdir in sorted(os.listdir(data_dir)):  # read subdir names
            if os.path.isdir(os.path.join(data_dir, subdir)):
                classes.append(subdir)

        self.classes = classes
        self.num_class = len(classes)
        ref_table_path = os.path.join(self.dir, 'ref_table.csv')

        # Construct CSV
        with open(ref_table_path, 'w') as csvfile:

            if six.PY2:
                delimiter = b','
                quotechar = b'|'

            else:
                delimiter = ','
                quotechar = '|'

            ref_table = csv.writer(csvfile,
                                   delimiter=delimiter,
                                   quotechar=delimiter,
                                   quoting=csv.QUOTE_MINIMAL)
            ["FILE_PATH, class_id, class_localization"]
            for root, dirs, files in os.walk(data_dir):
                print(root)
                class_name = os.path.basename(root)
                if class_name in classes:
                    class_idx = classes.index(class_name)
                    for file in files:
                        if '.jpg' in file:
                            ref_table.writerow([os.path.join(root, file),
                                                class_idx])

        return ref_table_path

    def _sample_decoder(self, path):
        """Decodes a sample from its path"""
        img = utils.load_img(path)
        img = utils.img_to_array(img)
        return img
