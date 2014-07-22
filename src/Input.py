__author__ = 'jchaudhary'

import os
import logging

CONST_EXTENSIONS = ['.ima', '.Ima', '.IMA', '.dcm', '.Dcm', '.DCM']
CONST_DATABASES = ['sql', 'sqlite', 'couch', 'couchdb']
logger = logging.getLogger('CrawlLogger.log')

class Input():
    def __init__(self, baseDirectory = None, extensions = CONST_EXTENSIONS, databases = CONST_DATABASES):
        if not os.path.isdir(baseDirectory):
            logger.warning('Invalid Directory: ' + baseDirectory)
            raise ValueError('Invalid Directory')
        else:
            self.baseDirectory = baseDirectory

        finalExtensions = []
        for ext in extensions:
            if ext in CONST_EXTENSIONS:
                finalExtensions.append(ext)
        self.extensions = finalExtensions

        finalDatabases = []
        for db in databases:
            if db in CONST_DATABASES:
                finalDatabases.append(db)
        self.databases = finalDatabases
        logger.info('Input Initialized')
        logger.debug('Extensions: ' + ', '.join(self.extensions))
        logger.debug('Databases: ' + ', '.join(self.databases))

'''
try:
    iin = Input('E:\works', extensions = ['ima', 'immma'], databases=['sql','sqlite', 'low'])
    print iin.baseDirectory
except:
    AttributeError
    print 'wrong directory'

print iin.extensions
print iin.databases
'''