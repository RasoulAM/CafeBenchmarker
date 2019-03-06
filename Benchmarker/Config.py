from abc import ABC, abstractmethod
import os

class Config(ABC):


    def __init__(self):
        self.classifier_name = ""
        self.train_time = 0
        self.model_size = 0
        self.test_time = 0
        self.accuracy = 0


    @abstractmethod
    def get_str(self):
        raise NotImplementedError

    @abstractmethod
    def get_dir(self):
        raise NotImplementedError

