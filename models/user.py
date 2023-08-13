#!/usr/bin/python3
'''inheritance of the user class finished '''
from models.base_model import BaseModel


class User(BaseModel):
    """ attributes of class User and the user is created"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

