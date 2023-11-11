#!/usr/bin/python3
"""
this module with purpose to test the class BaseModel
"""
import unittest
import models.base_model as base_model
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    implement test cases
    """

    # test documentation
    def test_doc(self):
        """test doc"""
        self.assertTrue(base_model.__doc__)
        self.assertTrue(base_model.BaseModel.__doc__)
        self.assertTrue(base_model.BaseModel.__init__.__doc__)
