#!/usr/bin/python3
"""The storage file is created today"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.state import State
from models.city import City
from models.place import Place


class FileStorage:
    """An abstract class of the file is created

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the oibject for the classes"""
        object_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = FileStorage.__objects
        object_dictionary = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(object_dictionary, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                object_dictionary = json.load(f)
                for o in object_dictionary.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            raise FileNotFoundError("File not found: {}".format(FileStorage.__file_path))



