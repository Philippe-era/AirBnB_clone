#!/usr/bin/python3
"""inheritance of the class I mean we up you check state"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class created in line with it"""

    name = ""

    def __init__(self, *args, **kwargs):
        """class prototype created """
        super().__init__(*args, **kwargs)

