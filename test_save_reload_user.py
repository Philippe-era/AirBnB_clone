#!/usr/bin/python3
from models import new_storage
from models.base_model import BaseModel
from models.user import User

all_object_created = new_storage.all()
print("-- Reloaded objects --")
for object_id in all_object_created.keys():
    obj_check = all_object_created[object_id]
    print(obj_check)

print("-- Create a new User --")
user_info = User()
user_info.first_name = "Betty"
user_info.last_name = "Holberton"
user_info.email = "airbnb@holbertonshool.com"
user_info.password = "root"
user_info.save()
print(user_info)

print("-- Create a new User 2 --")
user_info2 = User()
user_info2.first_name = "John"
user_info2.email = "airbnb2@holbertonshool.com"
user_info2.password = "root"
user_info2.save()
print(user_info2)

