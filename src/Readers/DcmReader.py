__author__ = 'jchaudhary'

from FileReader import FileReader

class DcmReader(FileReader):
    def __init__(self, file):
        super(DcmReader, self).__init__(file)

    def getRawData(self):
        pass