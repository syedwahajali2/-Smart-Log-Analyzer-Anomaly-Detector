from abc import ABC, abstractmethod
from typing import Any
class processor(ABC):
    """  today i create this project
    """
    def __init__(self, name, version):
        self._name = name
        self._version = version = "1.00"
    @property
    def name(self):
        return self._name
    @property
    def version(self):
        return self._version
    
    @abstractmethod
    def process(self):
        """ hi my name is wahaj"""
        pass
    
    @abstractmethod
    def summary (self):
        """ hello"""
        pass
    def __repr__(self):
        return f"{self.__class__.__name__} name ={self._name} version = {self._version}"
