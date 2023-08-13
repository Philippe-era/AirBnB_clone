#!/usr/bin/python3
"""inheritance of place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class created with its attributes"""

    city_id = ""
    user_id = ""
    name = ""
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    description = ""
    number_rooms = 0
    number_bathrooms = 0

    def __init__(self, *args, **kwargs):
        """initialzing of the super class place"""
        super().__init__(*args, **kwargs)

