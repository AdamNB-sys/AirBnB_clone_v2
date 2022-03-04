#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from os import getenv
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City', cascade='all, delete, delete-orphan', backref='state')
    else:
        @property
        def cities(self):
            """Getter for cities in filestorage"""
            from models import storage
            matched_obj = []
            for k in storage.all(City).values():
                if k.state_id == self.id:
                    matched_obj.append(k)
            return matched_obj
