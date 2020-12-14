#!/usr/bin/python3
""" Define new engine DBStorage
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage():
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                passwd, user, host, db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries for specified classes"""
        Session = sessionmaker()
        self.__session = Session(bind=self.__engine)
        object_dictionary = {}
        if cls is None:
            set_all_object = self.__session.query(User, City, Place, Review,
                                                  State, Amenity).all()
            for set_object in set_all_object:
                for obj in set_object:
                    object_dictionary[obj.to_dict()['__class__'] + '.' +
                                      obj.id] = obj
        else:
            set_objects = self.__session.query(cls).all()
            for obj in set_objects:
                object_dictionary[obj.to_dict()['__class__'] +
                                  '.' + obj.id] = obj
        return object_dictionary

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(engine)
        Session = scoped_session(sessionmaker(
                  bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
