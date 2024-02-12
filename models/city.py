#!/usr/bin/python3
"""This module contains City class that inherit from BaseModel."""

from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a City with state_id and name."""
    state_id = ""
    name = ""
