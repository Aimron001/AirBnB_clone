#!/usr/bin/python3
""" defines the Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ represents an amenity

    Attributes:
        name (str): the name of the Amenity
    """

    name = ""
