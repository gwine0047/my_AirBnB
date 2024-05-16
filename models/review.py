#!/usr/bin/python3
"""
Module for the review class
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
        Represent a review.

    Attributes:
        name (str): The name of the review.
    """
    text = ""
    place_id = "
    user_id = ""