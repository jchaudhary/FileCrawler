__author__ = 'jchaudhary'

from abc import ABCMeta, abstractmethod

class Database():
    __metaclass__ =ABCMeta
    def __init__(self, dbName):
        self.dbName = dbName

    @abstractmethod
    def setName(self):
        raise NotImplementedError()

    @abstractmethod
    def setConnection(self):
        raise NotImplementedError()

    @abstractmethod
    def insertData(self):
        raise NotImplementedError()

    @staticmethod
    def getDatabaseName(extension):
        return (extension[1:] + '_files_structured' )