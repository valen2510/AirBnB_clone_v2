#!/usr/bin/python3
"""unitest for testing City class """
import models
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State
from sqlalchemy.exc import OperationalError


class test_City(test_basemodel):
    """ Un"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_creation(self):
        """ """
        state = State(name="California")
        new = self.value(state_id=state.id, name="San_Francisco")
        self.assertEqual(type(new.state_id), str)
        self.assertEqual(type(new.name), str)
