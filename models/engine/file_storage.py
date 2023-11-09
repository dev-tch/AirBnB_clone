#!/usr/bin/python3
""" module with one class FileStorage"""
from models.base_model import BaseModel
from models.user import User
import json


class FileStorage:
    """implementation of class"""

    MapClass = {
        "BaseModel": BaseModel,
        "User": User
    }
    #  class attribute : string - path to the JSON file (ex: file.json)
    __file_path = "file.json"
    #  class attribute : dictionary - empty but will
    #  store all objects by <class name>.id
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__class__.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj and hasattr(obj, "id"):
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__class__.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict_json = {}
        for obj_id, obj_reference in self.__class__.__objects.items():
            dict_json[obj_id] = obj_reference.to_dict()
        with open(self.__class__.__file_path, "w", encoding="UTF-8") as fjson:
            json.dump(dict_json, fjson)

    def reload(self):
        """deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists ; otherwise, do nothing.
        """
        try:
            with open(self.__class__.__file_path, "r", encoding="UTF-8") as fj:
                # dict_obj = json.load(fjson)
                data = fj.read()
                if data:
                    dict_obj = json.loads(data)
                    for key, value in dict_obj.items():
                        str_class_name, str_obj_id = key.split(".")
                        cls = self.MapClass.get(str_class_name)
                        if cls:
                            create_obj_inst = cls(**value)
                            self.__class__.__objects[key] = create_obj_inst
        except FileNotFoundError:
            pass
