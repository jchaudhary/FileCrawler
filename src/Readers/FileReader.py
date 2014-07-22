__author__ = 'jchaudhary'

from abc import ABCMeta, abstractmethod
import os

class FileReader():
    __metaclass__ =ABCMeta
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def getRawData(self):
        raise NotImplementedError()

    @staticmethod
    def getFileExtension(file):
        return os.path.splitext(file)[1]