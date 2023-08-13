#!/usr/bin/python3
"""inheirance of the city classl"""
from models.base_model import BaseModel


class City(BaseModel):
    """The class is created based city class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """use of super to initialize the class"""
        super().__init__(*args, **kwargs)

