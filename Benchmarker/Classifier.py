from abc import ABC, abstractmethod
import os
import time

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


    def train_classifier(self, train_file):
        '''
            Train the classifier with all configs
            save all the models
        '''
        for config in self.config_list:
            print("Training classifier with following configuration:")
            start_time = time.time()
            model = self.train_classifier_with_config(train_file, config)
            print("Classifier trained with stated configuration")
            config.train_time = time.time() - start_time
            print("Training took %d seconds" % config.train_time)
            path = os.path.join(config.get_dir(), config.get_str())
            if not os.path.exists(config.get_dir()):
                os.makedirs(config.get_dir())
            if self.save_model(model, path):
                config.model_size = os.stat(path).st_size
                print("Model saved successfully")
            else:
                print("Model wasn't saved")
        
    
    @abstractmethod    
    def save_model(self, model, path):
        '''
            How to save a model of this classsifier to the given path
            return save status
        '''
        raise NotImplementedError 

    @abstractmethod
    def train_classifier_with_config(self, train_file, config):
        '''
            Train the model with the given cofiguration(hyperparameters)
            return the resulting model
        '''
        raise NotImplementedError
    
    def get_model(self, config):
        path = os.path.join(config.get_dir(), config.get_str())
        return self.load_model(path)

    @abstractmethod
    def load_model(self, path):
        '''
            How to load the model from given path 
        '''
        raise NotImplementedError

    def test_classifier(self, test_data):
        for config in self.config_list:
            model = self.get_model(config)
            start_time = time.time()
            config.accuracy = self.test_classifier_with_config(test_data, model)
            config.test_time = time.time() - start_time

        

    @abstractmethod
    def test_classifier_with_config(self, test_data, model):
        '''
            Test model with given config
            return accuracy
        '''
        raise NotImplementedError
    
    @abstractmethod
    def get_best_classifier(self):
        '''
            Return the best config and the best model
        '''
        raise NotImplementedError
