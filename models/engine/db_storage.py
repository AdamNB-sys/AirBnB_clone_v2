#!/usr/bin/python3
""" Storage engine to interact with MySQL database """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.base_model import Base
from os import getenv


class DBStorage:
    """class dbstorage for sql database"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiation of storage engine"""
        usr = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            usr, pwd, host, db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all instances"""
        valid_classes = [City, State, User, Place, Review]
        all_class = {}
        if cls in valid_classes:
            for k in self.__session.query(cls):
                all_class['{}.{}'.format(cls.__name__, k.id)] = k
        elif cls is None:
            for instance in valid_classes:
                for k in self.__session.query(instance):
                    all_class['{}.{}'.format(instance.__name__, k.id)] = k
        return all_class

    def new(self, obj):
        """Adds obj to current db session"""
        valid_classes = [City, State, User, Place, Review]
        if type(obj) in valid_classes:
            self.__session.add(obj)

    def save(self):
        """Commits all changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes object from the current database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates a database session from the engine"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        """calls remove method on private session attribute"""
        self.__session.remove()
