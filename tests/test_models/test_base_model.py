#!/usr/bin/python3
"""
this module with purpose to test the class BaseModel
"""
import unittest
import models.base_model as base_model
from models.base_model import BaseModel
import os
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    implement test cases
    """
    objBaseModel = None
    objBaseModel2 = None
    #  data test prepare and clean
    # setUpClass: common to all instances of test cases

    @classmethod
    def setUpClass(cls):
        """setup called af first class run"""
        cls.objBaseModel = BaseModel()
        cls.objBaseModel.name = "Tc"
        cls.objBaseModel.age = 32
        cls.objBaseModel2 = BaseModel(hobby="music", Job="software")
        cls.objBaseModel2.gender = "Male"

    @classmethod
    def teardown(cls):
        """run after end of class run"""
        del cls.objBaseModel
        del cls.objBaseModel2

    def tearDown(self):
        """called immediately after the test method has been called
        (after each testcase)
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
    # test documentation

    def test_docstring(self):
        """test documentation"""
        # module docstring
        self.assertTrue(base_model.__doc__)
        # class docstring
        self.assertTrue(base_model.BaseModel.__doc__)
        # methods
        self.assertTrue(base_model.BaseModel.__init__.__doc__)
        self.assertTrue(base_model.BaseModel.save.__doc__)
        self.assertTrue(base_model.BaseModel.to_dict.__doc__)
        self.assertTrue(base_model.BaseModel.__str__.__doc__)
        self.assertTrue(base_model.BaseModel.__str__.__doc__)

    def test_save(self):
        """ test method save """
        dt_creat_before = self.objBaseModel.created_at
        dt_update_before = self.objBaseModel.updated_at
        self.objBaseModel.save()
        dt_update_after = self.objBaseModel.updated_at
        dt_creat_after = self.objBaseModel.created_at
        self.assertGreater(dt_update_after, dt_update_before)
        self.assertEqual(dt_creat_before, dt_creat_after)

    def test_to_dict(self):
        """ test method to dict"""
        # Rule_1: returns a dictionary containing all
        #   keys/values of __dict__ of the instance
        # ---------------- test instance with dictionary ---------------

        result_dict = self.objBaseModel2.to_dict()
        self.assertIsInstance(result_dict, dict)
        # Rule_2: by using self.__dict__,
        #   only instance attributes set will be returned
        # Rules3: a key __class__ must be added to
        #   this dictionary with the class name of the object
        expected_dict = {"hobby": "music", "job": "software",
                         "gender": "Male", "__class__": "BaseMode"}
        sorted_result_dict = dict(sorted(result_dict.items()))
        expected_dict = dict(sorted(result_dict.items()))
        self.assertDictEqual(expected_dict, result_dict)

        # ---------------- test instance without dict --------------------

        result_dict = self.objBaseModel.to_dict()
        self.assertIsInstance(result_dict, dict)
        expected_keys = sorted(['name', 'age', 'created_at',
                                'updated_at', 'id', '__class__'])
        self.assertEqual(sorted(list(result_dict.keys())), expected_keys)
        self.assertEqual(result_dict["__class__"], 'BaseModel')
        # created_at and updated_at
        # must be converted to string object in ISO format
        self.assertIsInstance(result_dict['created_at'], str)
        self.assertIsInstance(result_dict['updated_at'], str)
        dt_cr_iso = datetime.strptime(result_dict['created_at'],
                                      "%Y-%m-%dT%H:%M:%S.%f")
        dt_up_iso = datetime.strptime(result_dict['updated_at'],
                                      "%Y-%m-%dT%H:%M:%S.%f")
        self.assertIsInstance(dt_cr_iso, datetime)
        self.assertIsInstance(dt_up_iso, datetime)
        self.assertEqual(self.objBaseModel.created_at, dt_cr_iso)
        self.assertEqual(self.objBaseModel.updated_at, dt_up_iso)

    def test__str__(self):
        """ test __str__"""
        # Rules
        # __str__: should print: [<class name>] (<self.id>) <self.__dict__>
        result_str = self.objBaseModel.__str__()
        name_cls = self.objBaseModel.__class__.__name__
        expected_str = "[] ({}) {}".format(name_cls,
                                           self.objBaseModel.id,
                                           self.objBaseModel.__dict__)
        self.assertEqual(result_str, result_str)
