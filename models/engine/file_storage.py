#!/usr/bin/python3
"""This is a module that contains the FileStorage that serializes instances to a JSON file and deserializes JSON file to instances."""

import json
import os.path
from models.ase_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """Class for serializing instances to a JSON file and deserializing from a JSON file."""

    __file_path = "file.json"
    __objects = {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

    def all(self):
        """Return the dictionary conatining all stored objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (__file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    class_obj = self.__objects[class_name]
                    obj_instance = class_obj(**obj_data)
                    self.__objects[key] = obj_instance
