#!/usr/bin/python3
"""This file defines the BaseModel Class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This class is a representation of the basemodel for airbnb clone project"""
    def __init__(self, *args, **kwargs):
        """The constructor, it initializes a new BaseModel"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """This func updates "updated_at" with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """This func returns the dictionary representation of the BaseModel instance/object"""
        ret_dict = self.__dict__.copy()
        ret_dict["created_at"] = self.created_at.isoformat()
        ret_dict["updated_at"] = self.updated_at.isoformat()
        ret_dict["__class__"] = self.__class__.__name__
        return ret_dict

    def __str__(self):
        """This func returns the str representation of the BaseModel instance/object"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
