__author__ = 'jchaudhary'

from FileReader import FileReader

class JpegReader(FileReader):
    def __init__(self, file):
        super(JpegReader, self).__init__(file)

    def getRawData(self):
        pass