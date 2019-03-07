import urllib.request
import os
import random

class Dataset():

    def __init__(self, path):
        # self.dataset_name = None
        self.dataset_path = path
        self.train_dataset_path = self.dataset_path + "_train_split"
        self.test_dataset_path = self.dataset_path + "_test_split"

    def split_train_and_test(self, path=None):
        with open(self.dataset_path, "r") as raw_dataset:
            with open(self.train_dataset_path, "w") as train_file:
                with open(self.test_dataset_path, "w") as test_file:
                    for line in raw_dataset:
                        if random.uniform(0, 1) > 0.1:
                            train_file.write(line)
                        else:
                            test_file.write(line)

class Benchmarker:  

    def __init__(self):
        self.datasets = []
        self.list_of_classifiers = None

    def add_dataset(self, dataset):
        self.datasets.append(dataset)

    # def set_classifiers(self, list_of_classifiers):
    #     self.list_of_classifiers = list_of_classifiers

    def add_classifier(self, new_classifier):
        if self.list_of_classifiers is None:
            self.list_of_classifiers = []
        new_classifier.set_data_path(self.datasets[0].train_dataset_path, self.datasets[0].test_dataset_path)
        self.list_of_classifiers.append(new_classifier)
        

    def clean_dataset(self, duplicate=True):
        '''
            clean the dataset, make another copy by default
        '''
        pass

    def train_all_classifiers(self):
        for classifier in self.list_of_classifiers:
            classifier.train_classifier()

    def report_stats(self):
        '''
            To be defined!!
        '''
        pass

