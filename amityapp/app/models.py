from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Persons(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    designation = Column(String(250), nullable=False)
    wants_accommodation = Column(String(10), nullable=False)


class Rooms(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    room_name = Column(String(250), nullable=False)
    room_type = Column(String(250), nullable=False)
