#!/usr/bin/python3
"""storage file created """
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """
   Storage file created 
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ instance of public function created
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Creation of relevant files related with assignment
        """
        if obj:
            key_storage = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key_storage] = obj

    def save(self):
        """
        Dictionary that creates the file.json file
        """
        new_dictionary = {}
        for key_check, value_check in FileStorage.__objects.items():
            new_dictionary[key_check] = value_check.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(new_dictionary, my_file)

    def reload(self):
        """
       JSON FILE DECENTRALIZED INTO IT
        """
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                new_dictionary = json.load(my_file)

            for key_check, value_check in new_dictionary.items():
                class_create = value_check.get('__class__')
                object_create = eval(class_create + '(**value_check)')
                FileStorage.__objects[key_check] = object_create

        except FileNotFoundError:
            pass

