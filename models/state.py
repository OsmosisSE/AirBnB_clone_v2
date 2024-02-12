#!/usr/bin/python3
"""This module contains State class that inherit from BaseModel."""

from models.base_model import BaseModel


class State(BaseModel):
    """Class representing a State with a name."""
    name = ""
