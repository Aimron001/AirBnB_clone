#!/usr/bin/python3
""" defines state class """
from models.base_model import BaseModel


class State(BaseModel):
    """represents the State class

    Attributes:
        name (str): The name of the state
    """

    name = ""
