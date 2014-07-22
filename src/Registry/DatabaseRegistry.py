__author__ = 'jchaudhary'

import os
import logging
from src.Databases.CouchDatabase import CouchDatabase
from src.Databases.SqlDatabase import SqlDatabase

logger = logging.getLogger('CrawlLogger.log')

class DatabaseRegistry():
    @staticmethod
    def getDatabase(db, dbName):
        if (db.lower() == 'sql'):
            logger.info('SQL DB OPERATIONS')
            return SqlDatabase(dbName)
        elif (db.lower() == 'couch' or db.lower == 'couchdb'):
            logger.info('COUCH DB OPERATIONS')
            return CouchDatabase(dbName)

