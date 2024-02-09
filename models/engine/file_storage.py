#!/usr/bin/python3
"""This is a module that contains the FileStorage that serializes instances to a JSON file and deserialize JSON file to instances."""

import json
from models.basemodel import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """Class for serializing instances to JSON file and deserializing from a JSON file."""

    __file_path = "file.json"
    __objects = {
                "BaseMode": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }

    def all(self):
        """Return the dictionary containing all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary.
        Args:
            obj: Instance of a class
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self, obj):
        """Serialize__objects to JSON file (__file_path)."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to dict() for obj in odict.keys()}
        with open(FileStorage.__filepath, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file to __objects.
        Only if the JSON file(__file_path) exists; otherwise do nothing.
        If the file doesn't, no exception should be raised.
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name =o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
