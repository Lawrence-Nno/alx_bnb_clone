#!/usr/bin/python3
"""Handles the Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Handles the review section of the site"""
    place_id = ""
    user_id = ""
    text = ""
