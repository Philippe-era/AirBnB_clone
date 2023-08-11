#!/usr/bin/python3
"""The base model class is created """
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """The class will be created necessarily"""

    def __init__(self, *args, **kwargs):
        """Constructor for the base class

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        the_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key_check, value_check in kwargs.items():
                if key_check == "created_at" or key_check == "updated_at":
                    self.__dict__[key_check] = datetime.strptime(value_check, the_form)
                else:
                    self.__dict__[key_check] = value_check
        else:
            models.storage.new(self)

    def save(self):
        """Updates the current context in which you are in"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns the necessary information needed
        """
        return_dictionary = self.__dict__.copy()
        return_dictionary["created_at"] = self.created_at.isoformat()
        return_dictionary["updated_at"] = self.updated_at.isoformat()
        return_dictionary["__class__"] = self.__class__.__name__
        return return_dictionary

    def __str__(self):
        """Returns the information required in this context ."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


