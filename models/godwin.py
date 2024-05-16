#!/usr/bin/python3

from models.base_model import BaseModel

class Godwin(BaseModel):
    # inheriting from BaseModel helps to define and use methods
    # that are not defined here in the class like __str__
    # to be able to use this in console.py, i will have to
    # include it in the list of valid classes
    """
    a class Godwin that inherits from BaseModel
    """
    def __init__(self):
        self.first_name = "Godwin"
        self.last_name = "Okoeguale"
        self.age = 33
        self.address = "63, Association Avenue, Palms City, New York"
        super().__init__(id)

    def __str__(self):
        return f'This is {self.first_name} {self.last_name}. I am {self.age} years old\nI live at {self.address}'