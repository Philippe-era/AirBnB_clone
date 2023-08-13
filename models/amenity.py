#!/usr/bin/python3
'''Base model created '''
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity class created"""

    name = ""

    def __init__(self, *args, **kwargs):
        """assigning the amenity class to something"""
        super().__init__(*args, **kwargs)

