#!/usr/bin/python3

"""Imports for the cmd hbnb command """
import cmd
import shlex
import models
from datetime import datetime
from models import new_storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    ]

    def do_create(self, argues):
        """Creates the necessary info for the function do create
        """
        argues = argues.split()
        if len(argues) == 0:
            print("** class name missing **")
        elif argues[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            create_file = eval(argues[0] + '()')
            models.storage.save()
            print(create_file.id)

    def do_show(self, argues):
        """the string will be printed 
        """
        string_check = argues.split()
        if len(string_check) == 0:
            print("** class name missing **")
        elif string_check[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(string_check) == 1:
            print("** instance id missing **")
        else:
            obj_check = models.storage.all()
            key_check = string_check[0] + '.' + string_check[1]
            if key_check in obj_check:
                print(obj_check[key_check])
            else:
                print("** no instance found **")

    def do_destroy(self, argues):
        """Deletes the instance created relevantly
        """
        argues = argues.split()
        object_check = models.storage.all()

        if len(argues) == 0:
            print('** class name missing **')
        elif argues[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argues) == 1:
            print('** instance id missing **')
        else:
            new_key = argues[0] + '.' + argues[1]
            if new_key in object_check.keys():
                object_check.pop(new_key, None)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, argues):
        """Displays all instances in strings representation
        """
        argues = argues.split()
        object_check = models.storage.all()
        new_array = []

        if len(argues) == 0:
            for obj in object_check.values():
                new_array.append(obj.__str__())
            print(new_array)
        elif argues[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in object_check.values():
                if obj.__class__.__name__ == argues[0]:
                    new_array.append(obj.__str__())
            print(new_array)

    def do_update(self, argues):
        """modifies information to make sure its up to date
        """
        object_check = models.storage.all()
        argues = argues.split(" ")

        if len(argues) == 0:
            print("** class name missing **")
        elif argues[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argues) == 1:
            print("** instance id missing **")
        elif len(argues) == 2:
            print("** attribute name missing **")
        elif len(argues) == 3:
            print("** value missing **")
        else:
            new_key = argues[0] + '.' + argues[1]
            obj = object_check.get(new_key, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, argues[2], argues[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def check_class_name(self, name=""):
        """checks whether the name is within the ranks"""
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """Checking the class  id """
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """Looks for name class."""
        if self.check_class_name(name):
            argues = shlex.split(name)
            if argues[0] in HBNBCommand.__classes:
                if self.check_class_id(name):
                    key_argue = argues[0] + '.' + argues[1]
                    return key_argue
                else:
                    print("** class doesn't exist **")
                    return None

    def do_quit(self, argues):
        """Exits program"""
        return True

    def do_EOF(self, argues):
        """Files handled by everything"""
        return True

    def emptyline(self):
        """checks empty string
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

