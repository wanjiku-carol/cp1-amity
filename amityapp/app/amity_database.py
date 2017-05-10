import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    designation = Column(String(250), nullable=False)
    wants_accommodation = Column(String(10), nullable=False)


class Room(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True)
    room_name = Column(String(250), nullable=False)
    room_type = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


engine = create_engine('sqlite:///amity.db')

Base.metadata.create_all(engine)
