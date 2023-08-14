#!/usr/bin/python3
from models import new_storage
from models.base_model import BaseModel

all_objects_created = new_storage.all()
print("-- Reloaded objects --")
for object_id in all_objects_created.keys():
    object = all_objects_created[object_id]
    print(object)

print("-- Create a new object --")
model_create = BaseModel()
model_create.name = "Holberton"
model_create.my_number = 89
model_create.save()
print(model_create)

