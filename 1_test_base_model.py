#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)

my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

dict_one = {
    "id" : "'e6d8089a-9f76-46de-b924-31d5647314a6",
    "updated_at" : "2024-05-08T11:08:15.113445",
    "__class__": "BaseModel",
    "created_at": "2024-05-08T11:09:21.839617"
}

print("\n\n\n")
new = BaseModel(**dict_one)
print(new)

# print("-----")
# print("--")
# my_new_model = BaseModel(**my_model_json)
# print(my_new_model.id)
# print(my_new_model)
# print(type(my_new_model.created_at))

# print("--")
# print(my_model is my_new_model)


