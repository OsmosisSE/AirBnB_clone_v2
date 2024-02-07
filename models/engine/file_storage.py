#!/usr/bin/python3
"""This is a module that contains the FileStorage that serializes instances to a JSON file and deserializes JSON file to instances."""

import json
from os import path

class FileStorage:
    """Class for serializing instances to a JSON file and deserializing from a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary conatining all stored objects.
        Returns:
                dict: Dictionary with objects stroed by <class name>.id.
        """

    def new(self, obj):
        """Adds a new object to the storage dictionary.
        Args:
            obj: The object to be added to the storage.
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (__file_path)."""
        obj_dict = {key: onj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects.
        If the JSON file (__file_path) exists, load the data into __objects.
        If the file doesn't exitst, do nothing (no exception should be raised).
        """

        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    obj_instance = class_obj(**obj_data)
                    self.__objects[key] = obj_instance
