#!/usr/bin/python3
"""This module conatins Amenity class that inherit from BaseModel."""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Class representing an Amenity with a name."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of Amenity."""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
