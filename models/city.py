#!/usr/bin/python3
"""This module contains City class that inherit from BaseModel."""

from models.base_model import BaseModel

class City(BaseModel):
    """Class representing a City with state_id and name."""
    
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of City."""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', "")
        self.name = kwargs.get('name', "")
