__author__ = 'jchaudhary'

__author__ = 'jchaudhary'

from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
from Databases.DeclarativeBase import SOPInstanceUID, Modality, FileLocation, Base

engine = create_engine('sqlite:///ima_files_structured.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


sopInstanceUID = '1.3.12.2.1107.5.2.19.45639.2014032415405495770344917'



temp = session.query(SOPInstanceUID)[3]
print temp.sopInstanceUID
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[0].location
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[0].sopId
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[0].fileSequenceNumber

print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[1].location
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[1].sopId
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[1].fileSequenceNumber

print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[2].location
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[2].sopId
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[2].fileSequenceNumber

print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[3].location
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[3].sopId
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[3].fileSequenceNumber

print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[4].location
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[4].sopId
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[4].fileSequenceNumber

print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[5].location
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[5].sopId
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[5].fileSequenceNumber
'''

print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[12].location
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[12].sopId
print session.query(FileLocation).filter(FileLocation.sopInstanceUID == temp)[12].fileSequenceNumber
'''
'''
'''
print '************'
print len(session.query(FileLocation).all())
print session.query(Modality).all()
print len(session.query(SOPInstanceUID).all())
print '************'

