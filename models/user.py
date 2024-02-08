#!/usr/bin/python3
"""This module defines the User class that inherits from BaseModel."""

from models.base_model import BaseModel

class User(BaseModel):
    """Class representing a User with email, password, first_name and last_name."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
