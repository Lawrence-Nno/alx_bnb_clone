#!/usr/bin/python3
"""This file handles the FileStorage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class handles the storage engine capacities"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary instantiated objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """This method serializes __objects to the JSON file __file_path"""
        odict = FileStorage.__objects
        obj_dict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """This method deserializes the JSON file __file_path to __objects if it exits"""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for ob in obj_dict.values():
                    cls_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(cls_name))(**ob)
        except FileNotFoundError:
            return
