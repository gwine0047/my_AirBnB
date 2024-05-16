#!/usr/bin/python3
from models.base_model import BaseModel

first_model = BaseModel()
first_model.name = "My first model"
first_model.my_number = 700
first_model.save()
print(first_model)