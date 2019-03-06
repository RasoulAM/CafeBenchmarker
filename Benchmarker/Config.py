from abc import ABC, abstractmethod
import os

class Config(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_str(self):
        raise NotImplementedError

    @abstractmethod
    def get_path(self):
        raise NotImplementedError

