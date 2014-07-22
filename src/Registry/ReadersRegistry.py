__author__ = 'jchaudhary'

from src.Readers import ImaReader, JpegReader, DcmReader
import os
import logging

logger = logging.getLogger('CrawlLogger.log')
class ReadersRegistry():
    @staticmethod
    def getReader(file):
        ext = (os.path.splitext(file)[1]).lower()
        if (ext == '.ima' ):
            logger.info('File Reader found: ImaReader()')
            return ImaReader.ImaReader(file)
        elif (ext == '.dcm'):
            logger.info('File Reader found: DcmReader()')
            return DcmReader.DcmReader(file)
        elif (ext == '.jpeg'):
            logger.info('File Reader found: JpegReader()')
            return JpegReader.JpegReader(file)
