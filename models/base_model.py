#!/usr/bin/python3
"""Defines a class containing common attributes,
and methods for other classes"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """implements a BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Iniatializes the basemodel class

        Args:
            *args (any type): arguements
            **kwargs (dict): key and value pairs
        """
        tm_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tm_format)
                else:
                    self.__dict__[key] = value

    def save(self):
        """updates the updated_at attribute"""
        updated_at = datetime.today()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """defines how the class objects are printed"""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
