#!/usr/bin/python3
""" defines the City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ represents the city class

    Attributes:
        state_id (str): The state's ID
        name (str): The name of the city
    """

    state_id = ""
    name = ""
