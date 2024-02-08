#!/usr/bin/python3
"""This module contains Review class that inherit from BaseModel."""

from models.base_model import BaseModel

class Review(BaseModel):
    """Class representing a Review with place_id, user_id and text."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of Review."""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.text = kwargs.get('text', "")
