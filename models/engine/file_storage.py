#!/usr/bin/python3
"""Defines a FileStorage Class"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """implements serialization and deserialization of JSON file

    Attributes:
        __file_path (str): path to JSON file
        __objects (dict): a dict to store all objects
        """
    __file_path = "file.json"
    __objects = {}

    def all(Self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        o_cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(o_cls_name, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        tmpdict = FileStorage.__objects
        objdict = {obj: tmpdict[obj].to_dict() for obj in tmpdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
