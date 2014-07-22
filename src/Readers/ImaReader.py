__author__ = 'jchaudhary'

from FileReader import FileReader
import dicom
import simplejson
import logging
import os

CONST_MODALITY = 0x8,0x60
CONST_SLICE_RESOLUTION = 0x19,0x1017
logger = logging.getLogger('CrawlLogger.log')

class ImaReader(FileReader):
    def __init__(self, file):
        """
        Initializing the class
        :param file: the absolute path of the file
        """
        if not os.path.exists(file):
            raise IOError('Given file does not exist')
        else:
            super(ImaReader, self).__init__(file)
        self.ds = dicom.read_file(file)
        logger.info('ImaReader() Initialized')
        logger.debug('ImaReader: ' + file)

    def getRawData(self):
        """
        A method to return the parameters that we need to extract from the give ima file.
        The parameters constitute the SOPInstanceUID, Modality, File name etc.
        :return: the dictionary with the parameters as keys and their values read from the file.
        """
        id =self.ds.data_element("SOPInstanceUID").value
        mod = self.ds[CONST_MODALITY].value
        res = simplejson.dumps(simplejson.Decimal(self.ds[CONST_SLICE_RESOLUTION].value),use_decimal=True)
        logger.info('Preparing raw data:')
        logger.debug('SOPInstanceUID:' + id + '|' + 'File: ' + self.file + '|' + 'Modality: ' + mod + '|' + 'SliceResolution: ' + res)
        return {
            '_id': id,
            'File': [self.file],
            'Modality': mod,
            'SliceResolution': res
        }


'''
file = r"\\gaia\fme\home\akoehn\public\4Joshan\MiDbTest\NaKoE_723_0022_000001.ima"
iread = ImaReader(file)
print iread.file
print iread.getRawData()
'''