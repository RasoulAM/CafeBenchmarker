from abc import ABC, abstractmethod
import os

class Classifier(ABC):

    '''
        This is a multi-config classifier.
        It stores a list of configurations when initialized.
        It can train the model with all the different configurations.
        Is able to return the best classifier
    '''

    def __init__(self, classifier_name, train_dataset_path, test_dataset_path, config_list):
        self.classifier_name = classifier_name
        self.path = os.path.join('models', classifier_name)
        self.train_dataset_path = train_dataset_path
        self.test_dataset_path = test_dataset_path
        self.config_list = config_list

    @abstractmethod
    def preprocess_dataset(self, dataset):
        '''
            Reads the dataset and returns a preprocessed version of it.
            #TODO specify the returned format (csv, json, pandas dataframe, any at all,...?)
        '''
        raise NotImplementedError

    @abstractmethod
    def preprocess_dataset_and_write(self, dataset):
        '''
            Reads the dataset, preprocesses it and writes it to file
        '''
        raise NotImplementedError

    def train_classifier(self, train_file):
        '''
            Train the classifier with all configs
            save all the models
        '''
        pass

    @abstractmethod
    def train_classifier_with_config(self, train_file, config):
        '''
            Train the model with the given cofiguration(hyperparameters)
            return thr resulting model
        '''
        raise NotImplementedError
    
    def get_model(self, config):
        '''
            Return the model corresponding to this configuration
        '''
        pass

    def test(self, test_data):
        '''
            Test all the models with the test data
            Save all the results
        '''
        pass

    @abstractmethod
    def test_model(self, test_data, config):
        '''
            Test model with given config
            return ?
        '''
        raise NotImplementedError
    
    @abstractmethod
    def get_best_classifier(self):
        '''
            Return the best config and the best model
        '''
        raise NotImplementedError
