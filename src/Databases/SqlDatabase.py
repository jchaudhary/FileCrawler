__author__ = 'jchaudhary'

from Database import Database
import logging
from DeclarativeBase import DeclarativeBase, Base, SOPInstanceUID, Modality, FileLocation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy

logger = logging.getLogger('CrawlLogger.log')

class SqlDatabase(Database):
    def __init__(self, dbName):
        dbName = r'sqlite:///' + dbName + r'.db'
        super(SqlDatabase, self).__init__(dbName)
        logger.debug('Database Name: ' + dbName)
        engine = create_engine(self.dbName)
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        self.session = session

    def setName(self, dbName):
        super(SqlDatabase, self).__setattr__(dbName, dbName)
        logger.debug('Sql database name changed to: ' + dbName)

    def setConnection(self):
        base = DeclarativeBase(self.dbName)
        base.create()
        logger.info('Declarative Base initialized: Tables initialized')


    def getSession(self):
        engine = create_engine(self.dbName)
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        return session

    def insertData(self, rawData, db):
        db.setConnection()

        #adding SOPInstanceUID and FileLocation
        try:
            new_id = SOPInstanceUID(sopInstanceUID=rawData.get('_id'))
            self.session.add(new_id)
            self.session.commit()
            logger.debug('New SOPInstanceUID added: ' + str(new_id))
        except:
            sqlalchemy.exc.IntegrityError
            logger.error('Duplicate SOPInstanceUID: ' + str(new_id) )
            logger.info('Update FileLocation Initializing.')
            self.session.rollback()
            tempSop = self.session.query(SOPInstanceUID).filter(SOPInstanceUID.sopInstanceUID == rawData.get('_id')).one()
            lengthSeqNum = len(self.session.query(FileLocation).filter(FileLocation.sopInstanceUID == tempSop).all())
            try:
                update_files = FileLocation(fileSequenceNumber = lengthSeqNum + 1, location = rawData.get('File')[0],sopInstanceUID = tempSop)
                self.session.add(update_files)
                self.session.commit()
                logger.debug('File Location updated: ' + str(update_files))
            except:
                sqlalchemy.exc.IntegrityError
                logger.info('Duplicate file location')
        else:
            try:
                new_file = FileLocation(fileSequenceNumber = 1, location = rawData.get('File')[0],sopInstanceUID = new_id)
                self.session.add(new_file)
                self.session.commit()
                logger.debug('New FileLocation added: ' + str(new_file))
            except:
                sqlalchemy.exc.IntegrityError
                self.session.rollback()
                logger.info('FileLocation already exists: ' + str(new_file))

        #adding Modality
        try:
            new_modality = Modality(modality = rawData.get('Modality'))
            self.session.add(new_modality)
            self.session.commin()
            logger.debug('New Modality added: ' + str(new_modality))
        except:
            sqlalchemy.exc.IntegrityError
            self.session.rollback()
            logger.info('Modality already exists: ' + str(new_modality))


'''
db = SqlDatabase('ima_files_structured')
db.setConnection()
'''