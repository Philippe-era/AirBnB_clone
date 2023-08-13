#!/usr/bin/python3
'''Inhirentance of the Review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class created in this line"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Review being initialized into the structure of it"""
        super().__init__(*args, **kwargs)

