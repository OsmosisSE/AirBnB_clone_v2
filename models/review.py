#!/usr/bin/python3
"""This module contains Review class that inherit from BaseModel."""

from models.base_model import BaseModel

class Review(BaseModel):
    """Class representing a Review with place_id, user_id and text."""
    place_id = ""
    user_id = ""
    text = ""
