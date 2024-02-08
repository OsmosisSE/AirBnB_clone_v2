#!/usr/bin/python3
"""This module contains State class that inherit from BaseModel."""

from models.base_model import BaseModel

class State(BaseModel):
    """Class representing a State with a name."""
    
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of State."""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
