#!/usr/bin/python3
""" defines Review class """
from models.base_model from BaseModel


class Review(BaseModel):
    """ represents Review

    Attributes:
        place_id (str): The place ID
        user_id (str): The user ID
        text (str): text
    """
    place_id = ""
    user_id = ""
    text = ""
