__author__ = 'jchaudhary'


from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DeclarativeBase():
    def __init__(self, dbName):
        self.dbName = dbName

    def create(self):
        engine = create_engine(self.dbName)
        Base.metadata.create_all(engine)

class SOPInstanceUID(Base):
    __tablename__ = 'sopInstanceUID'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sopInstanceUID = Column(String, nullable=False, unique=True)

class Modality(Base):
    __tablename__ = 'modality'
    id = Column(Integer, primary_key=True)
    modality = Column(String, unique=True)

class FileLocation(Base):
    __tablename__ = 'fileLocation'
    id = Column(Integer, primary_key=True)
    sopId = Column(String, ForeignKey('sopInstanceUID.id'))
    fileSequenceNumber = Column(Integer)
    location = Column(String, unique=True)
    sopInstanceUID = relationship(SOPInstanceUID)

'''
dbName = 'sqlite:///joshan.db'
db = DeclarativeBase(dbName)
engine = create_engine(db.dbName)
Base.metadata.create_all(engine)

'''