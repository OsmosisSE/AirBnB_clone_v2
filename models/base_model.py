#!/usr/bin/python3
"""This is a model for Base class that defines all common attributes/methods for other classes."""

import uuid
from datetime import datetime

class BaseModel:
    """Base class for other models with common attributes and methods."""
    def __init__ = (self):
        """Initialize a new instance of the BaseModel class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the 'update_at' attribute with the current datetime."""
        self.update_at = datetime.now()

    def to_dict(self):
        """Return a dictionary represention of the instance.
        Returns:
            dict: A dictionary containing keys/values of instance attributes.
                    Includes '__class__', 'created_at' and 'updated_at.'
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isofarmat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Return a dictionary reprsentation of the instance.
        Returns:
            str: A string in the format: "[<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
