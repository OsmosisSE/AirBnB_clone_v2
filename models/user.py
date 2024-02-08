#!/usr/bin/python3
"""This module defines the User class that inherits from BaseModel."""

from models.base_model import BaseModel

class User(BaseModel):
    """Class representing a User with email, password, first_name and last_name."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of User."""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")
