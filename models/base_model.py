#!/usr/bin/python3
""" module with one class BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """implement class BaseModel"""

    def __init__(self, *args, **kwargs):
        """constructor method
        Args:
            id(str): unique id of an object
            create_at(datetime): date and time  of creation new  instance
            updated_at(datetime): dat and time of
            updating already created instance
        """
        # case1 : kwargs is not empty
        if kwargs:
            if not isinstance(kwargs, dict):
                return
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)  # new object not from dictionary

    def __str__(self):
        """ string representation of an object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()  # convert storage to json file

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
         of __dict__ of the instance
        """
        dict_obj = self.__dict__.copy()
        if ("created_at" in dict_obj and
                isinstance(dict_obj["created_at"], datetime)):
            dict_obj["created_at"] = dict_obj["created_at"].isoformat()
        if ("updated_at" in dict_obj
                and isinstance(dict_obj["updated_at"], datetime)):
            dict_obj["updated_at"] = dict_obj["updated_at"].isoformat()
        dict_obj["__class__"] = self.__class__.__name__
        return dict_obj
