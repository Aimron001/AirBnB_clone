#!/usr/bin/python3
"""Defines unittests classes for base_model.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittest for testing instantiation ofobject of the BaseModel class."""

    def test_empty_instance(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datetimeobj(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_datetimeobj(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_is_unique_ids(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_unused_args(self):
        obj = BaseModel(None)
        self.assertNotIn(None, obj.__dict__.values())


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing the public class save method"""

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)


    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        obj = BaseModel()
        self.assertTrue(dict, type(obj.to_dict()))

    def test_to_dict_has_correct_keys(self):
        obj = BaseModel()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())

    def test_to_dict_contains_added_attrs(self):
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 98
        self.assertIn("name", obj.to_dict())
        self.assertIn("my_number", obj.to_dict())

    def test_to_dict_datetime_attrs_are_strs(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(str, type(obj_dict["created_at"]))
        self.assertEqual(str, type(obj_dict["updated_at"]))

    def test_to_dict_return(self):
        dt = datetime.today()
        obj = BaseModel()
        obj.id = "123456"
        obj.created_at = obj.updated_at = dt
        bdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(obj.to_dict(), bdict)

    def test_difference_to_dict_dunder_dict(self):
        obj = BaseModel()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_to_dict_args(self):
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.to_dict(None)


if __name__ == "__main__":
    unittest.main()
