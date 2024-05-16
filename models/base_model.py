#!/usr/bin/python3

"""
This can be used as a base for other classes to use
and inherit from it attributes and methods such as unique identifiers
managing and updating time and providing serialization capabilities
"""
import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    # let's grab the key word arguments if provided
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

        # whenever an instance of basemodel is call, it is passed to the 
        # FileStorage methof through an instance storage which is also
        # instantiated inside the init file of models

        models.storage.new(self)
    def save(self):
        """
        updates self.updated _at
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        serialization: turning obj to a dictionary
        """
        # self.__dict__ is a built in attribute and it is
        # automatically created for every instance of a class
        instance_dict_copy = self.__dict__.copy()

        instance_dict_copy["__class__"] = self.__class__.__name__
        instance_dict_copy["created_at"] = self.created_at.isoformat()
        instance_dict_copy["updated_at"] = self.updated_at.isoformat()

        return instance_dict_copy

    def __str__(self):
        """
        what the instance should display when printed
        """
        class_name = self.__class__.__name__
        return f'\t\tSTRING REPRESENTATION OF BASEMODEL OBJECT\n\n[class = {class_name}]\n(instance id = {self.id}\nThis instance was created at = {self.created_at.isoformat()}\n\n{self.__dict__})'

