#!/usr/bin/python3
"""
Module for the city class
"""
from models.base_model import BaseModel

class City(BaseModel):
    """
        Represent a city.

    Attributes:
        name (str): The name of the city.
        state_id (str): The state it belongs
    """
    name = ""
    state_id = ""