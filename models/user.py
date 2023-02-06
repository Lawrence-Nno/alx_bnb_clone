#!/usr/bin/python3
"""This file handles the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
