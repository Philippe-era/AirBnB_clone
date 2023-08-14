#!/usr/bin/python3
"""base model created in this instance"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """base model created in this"""
    def __init__(self, *args, **kwargs):
        """base model class constructor """
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            for key_check, value_check in kwargs.items():
                if key_check != '__class__':
                    setattr(self, key_check, value_check)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.new_storage.new(self)

    def __str__(self):
        """string for base model class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """modified information regarding time and date"""
        self.updated_at = datetime.now()
        models.new_storage.save()

    def to_dict(self):
        """delete dictionary  info"""
        dictionary_create = dict(self.__dict__)
        dictionary_create['created_at'] = self.__dict__['created_at'].isoformat()
        dictionary_create['updated_at'] = self.__dict__['updated_at'].isoformat()
        dictionary_create['__class__'] = self.__class__.__name__
        return (dictionary_create)

