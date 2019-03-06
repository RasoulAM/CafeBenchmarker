import urllib.request
import os

class Benchmarker:  

    def __init__(self):
        self.dataset_name = None
        self.dataset_path = None
        self.train_dataset = None
        self.test_dataset = None
        self.list_of_classifiers = None

    def set_dataset(self, pointer_to_the_dataset):
        '''
            Set the pointer to the dataset
        '''
        pass

    def split_train_and_test(self):
        '''
            Splits the dataset to train and test
        '''
        pass

    def set_default_dataset(self):
        dataset_url = 'some_url'
        dataset_directory = './dataset'
        self.dataset_name = 'raw_data.json'
        self.dataset_path = os.path.join(dataset_directory, self.dataset_name)
        urllib.request.urlretrieve(dataset_url, self.dataset_path)

    def set_classifiers(self, list_of_classifiers):
        self.list_of_classifiers = list_of_classifiers

    def add_classifier(self, new_classifier):
        if self.list_of_classifiers is None:
            self.list_of_classifiers = []
        self.list_of_classifiers.append(new_classifier)
        

    def clean_dataset(self, duplicate=True):
        '''
            clean the dataset, make another copy by default
        '''
        pass

    def train_all_classifiers(self):
        '''
            this method will train all the models and store them in the models directory
        '''
        pass

    def report_stats(self):
        '''
            To be defined!!
        '''
        pass    

