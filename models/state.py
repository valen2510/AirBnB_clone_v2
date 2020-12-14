#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state') 

    @property
    def cities(self):
        """Getter attribute cities that returns the list of City instances"""
        from models import storage
        new_list = []
        for key, obj_city in storage.all(City).items():
            if obj_city.state_id == self.id:
                new_list.append(obj_city)
        return new_list
