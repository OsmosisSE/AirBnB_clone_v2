#!/usr/bin/python3
"""This is a model for Base class that defines all common attributes/methods for other classes."""

import uuid
from datetime import datetime

class BaseModel:
    """Base class for other models with common attributes and methods."""
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class.
        Args:
            *args: The variable-length argument list (not used in this implementation).
            **kwargs: The variable-length keyword argument list.
                If not emepty, each key is an attribute name, and each value is a corresponding value
                'created_at' and 'updated_at' values are converted from strings to datetime objects.
                'id' is set to a new UUID if not present.
                '__class__' from kwargs is ignored
        """

        if kwargs:
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs['updated_at'], kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")

            kwargs.pop('__class__', None)
            kwargs.pop('id', None)
            kwargs.pop('created_at', None)
            kwargs.pop('updated_at', None)

            for key, value in kwargs.items():
                setattr(self, key, value)
        else:        
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
