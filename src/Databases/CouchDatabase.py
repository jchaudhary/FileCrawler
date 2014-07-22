__author__ = 'jchaudhary'

from Database import Database
import logging
import couchdb

logger = logging.getLogger('CrawlLogger.log')
CONST_ADDRESS = r"http://127.0.0.1:5984/"

class CouchDatabase(Database):
    def __init__(self, dbName):
        super(CouchDatabase, self).__init__(dbName)
        logger.debug('Database name: ' + dbName)
        self.address = CONST_ADDRESS
        self.server = couchdb.Server(self.address, full_commit=True)

    def setName(self, dbName):
        super(CouchDatabase, self).__setattr__(dbName, dbName)
        logger.debug('Couchdb name changed to: ' + dbName)

    def setAddress(self, address):
        self.address = address

    def setServer(self):
        self.server = couchdb.Server(self.address, full_commit=True)

    def setConnection(self):
        try:
            dbObject = self.server.create(self.dbName)
            logger.debug('Database created: ' + self.dbName)
        except:
            couchdb.PreconditionFailed
            dbObject = self.server[self.dbName]
            logger.debug('Database choosen: ' + self.dbName)
        return dbObject

    def insertData(self, rawData, db):
        dbObject = db.setConnection()
        try:
            result = dbObject.save(rawData)
            logger.debug('Data Inserted: ' + rawData)
            return result
        except:
            couchdb.ResourceConflict
            doc = dbObject.get(rawData.get('_id'))
            tempFile = rawData.get('File')
            existingFile = doc.get('File')

            if tempFile[0] in existingFile:
                logger.info('Nothing to add here!!')
            else:
                doc['File'] = existingFile + tempFile
                doc = dbObject.save(doc)
                logger.debug('Updating Database: ' + str(doc))
                return doc


'''
rawData = {'_id': '1.3.12.2.1107.5.2.19.45639.2014032415405495770344917',
           'Modality': 'MR',
           'File': '\\gaia\fme\home\akoehn\public\4Joshan\MiDbTest\NaKoE_723_0022_000001.ima',
           'SliceResolution': '1'}

couch = CouchDatabase('ima_files_check')
db = couch.setConnection()
print couch.insertData(rawData, db)
'''