#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    # the below is used to store objects using cllass_name.id
    __objects = {}

    def new(self, obj):
        """
        use to add new instant objects to __objects
        obj: is the instant obj
        """
        obj_cls_name = obj.__class__.__name__
        # remember the objs have to stored using class_name.id
        key = f'{obj_cls_name}.{obj.id}'
        FileStorage.__objects[key] = obj

    def all(self):
        """
        retrieves all objects stored in 
        Filestorage.__objects
        """
        return FileStorage.__objects

    def save(self):
        """
        saves the objects in JSON format - 
        serializes a dictionary
        """
        # access all the objects
        all_objs = FileStorage.__objects
        # iterate through the keys and store them as JSON in obj_dict
        obj_dict = {}
        # for each obj_key in all_objs, the value is serialize using to dict()
        # and the using the same key in the obj_dict, a serialized value is passed.
        for obj_key in all_objs.keys():
            obj_dict[obj_key] = all_objs[obj_key].to_dict()

        # now write those values in a file as json
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        deserializes a json file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    # deserialize using load
                    obj_dict = json.load(file)
                    # iterate through the keys and values
                    for key, value in obj_dict.items():
                        # remember keys=basename.id, split keys into basename(class_name) and id
                        class_name, obj_id = key.split('.')
                        # eval the class_name 
                        cls = eval(class_name)
                        # create an instance using the class_name and passing the values as **kwargs
                        # remember our basemodel class can accept key word arguments
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass