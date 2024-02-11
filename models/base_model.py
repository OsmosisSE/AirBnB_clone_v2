#!/usr/bin/python3
"""Defines the BaseModel class."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class for other models with common attributes and methods."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class.

        Args:
            *args: Not used in this implementation.
            **kwargs: The variable-length keyword argument list.
            If not empty, each key is an attribute name, and each value
            is a corresponding value
                'created_at' and 'updated_at' values are converted
                from strings to datetime objects.
                'id' is set to a new UUID if not present.
                '__class__' from kwargs is ignored
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, tform))
                elif k != "__class__":
                    setattr(self, k, v)

    def save(self):
        """Update the 'update_at' attribute with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary represention of the instance."""
        rdict = self.__dict__.copy()
        rdict['__class__'] = self.__class__.__name__
        rdict['created_at'] = self.created_at.isoformat()
        rdict['updated_at'] = self.updated_at.isoformat()
        return rdict

    def __str__(self):
        """Return a string reprsentation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
