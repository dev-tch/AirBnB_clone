#!/usr/bin/python3
""" module with one class BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """implement class BaseModel"""

    # public instance id

    def __init__(self):
        """constructor method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ string representation of an object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
         of __dict__ of the instance
        """
        dict_obj = self.__dict__.copy()
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()
        dict_obj["__class__"] = self.__class__.__name__
        return dict_obj
