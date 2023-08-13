#!/usr/bin/python3
from models.base_model import BaseModel

model_create = BaseModel()
model_create.name = "Holberton"
model_create.my_number = 89
print(model_create.id)
print(model_create)
print(type(model_create.created_at))
print("--")
model_create_json = model_create.to_dict()
print(model_create_json)
print("JSON of model_create:")
for key_check in model_create_json.keys():
        print("\t{}: ({}) - {}".format(key_check, type(model_create_json[key_check]),
                                       model_create_json[key_check]))

        print("--")
        model_create_new = BaseModel(**model_create_json)
        print(model_create_new.id)
        print(model_create_new)
        print(type(model_create_new.created_at))

        print("--")
        print(model_create is model_create_new)

