#!/usr/bin/python3
"""This module conatins Amenity class that inherit from BaseModel."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing an Amenity with a name."""
    name = ""
