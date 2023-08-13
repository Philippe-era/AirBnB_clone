#!/usr/bin/python3
from models.base_model import BaseModel

model_create = BaseModel()
model_create.name = "Holberton"
model_create.my_number = 89
print(model_create)
model_create.save()
print(model_create)
model_create_json = model_create.to_dict()
print(model_create_json)
print("JSON of my_model:")
for key_check in model_create_json.keys():
    print("\t{}: ({}) - {}".format(key_check, type(model_create_json[key_check]),
                                   model_create_json[key_check]))

