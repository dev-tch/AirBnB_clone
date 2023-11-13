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
    #  data test prepare and clean
    # setUpClass: common to all instances of test cases

    @classmethod
    def setUpClass(cls):
        """setup called af first class run"""
        cls.objBaseModel = BaseModel()
        cls.objBaseModel.name = "Tc"
        cls.objBaseModel.age = 32

    @classmethod
    def teardown(cls):
        """run after end of class run"""
        del cls.objBaseModel

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
        dt_creat_before = self.objBaseModel.created_at
        dt_update_before = self.objBaseModel.updated_at
        self.objBaseModel.save()
        dt_update_after = self.objBaseModel.updated_at
        dt_creat_after = self.objBaseModel.created_at
        self.assertGreater(dt_update_after, dt_update_before)
        self.assertEqual(dt_creat_before, dt_creat_after)
