#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id',
                             String(60), ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities",
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """Getter for reviews in filestorage"""
            from models import storage
            matched_obj = []
            for k in storage.all(Review).values():
                if k.place_id == self.id:
                    matched_obj.append(k)
            return matched_obj

        @property
        def amenities(self):
            """Getter for amenities in filestorage"""
            from models import storage
            matched_obj = []
            for k in storage.all(Amenity).values():
                if k.id == self.amenities_ids:
                    matched_obj.append(k)
            return matched_obj

        @amenities.setter
        def amenities(self, value):
            """appends new amenity id to amenity_ids list"""
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
