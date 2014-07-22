__author__ = 'jchaudhary'

from Input import Input
from Readers.FileReader import FileReader
import logging
import logging.handlers
from Databases.Database import Database
from Databases.SqlDatabase import SqlDatabase
from Registry.ReadersRegistry import ReadersRegistry
from Registry.DatabaseRegistry import DatabaseRegistry
import os

LOG_FILENAME = 'CrawlLogger.log'
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logger = logging.getLogger(LOG_FILENAME)

handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=5242880, backupCount=3)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(FORMAT)
ch.setFormatter(formatter)
handler.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(handler)

CONST_DB_NAME = None

try:
    iin = Input(r"\\gaia\fme\home\akoehn\public\4Joshan\MiDbTest", extensions = ['.ima', '.immma'], databases=['couch','sql','low'])
except:
    ValueError
else:
    for tempExt in iin.extensions:
        for tempDb in iin.databases:
            CONST_DB_NAME = Database.getDatabaseName(tempExt)
            db = DatabaseRegistry.getDatabase(tempDb, CONST_DB_NAME)
            '''if isinstance(db, SqlDatabase):
                session = db.getSession()
            else:
                session = None'''
            for root, dirs, files in os.walk(iin.baseDirectory):
                for fileTemp in files:
                    if (FileReader.getFileExtension(fileTemp) == tempExt):
                        absFile = os.path.join(root, fileTemp)
                        try:
                            reader = ReadersRegistry.getReader(absFile)
                            rawData = reader.getRawData()
                        except:
                            IOError
                        else:
                            db.insertData(rawData,db)

logger.info('***********************************************************************')