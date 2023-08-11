#!/usr/bin/python3

"""Defines the HBnB console."""
import cmd
import re
from models.amenity import Amenity
from models.review import Review
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place


def parse(arg):
    curly_brackets = re.search(r"\{(.*?)\}", arg)
    braces = re.search(r"\[(.*?)\]", arg)
    if curly_brackets is None:
        if braces is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexus = split(arg[:braces.span()[0]])
            reload = [i.strip(",") for i in lexus]
            reload.append(braces.group())
            return reload
    else:
        lexus = split(arg[:curly_braces.span()[0]])
        reload = [i.strip(",") for i in lexus]
        reload.append(curly_braces.group())
        return reload

class HBNBCommand(cmd.Cmd):
    """The HBNB WILL BE DEFINED
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """DOES NOTHING WHEN THERE IS NO INFORMATION."""
        pass

    def default(self, arg):
        """BEHAVIOUR IS DONE UNJUSTLY """
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        similar = re.search(r"\.", arg)
        if similar is not None:
            argue_line = [arg[:similar.span()[0]], arg[similar.span()[1]:]]
            similar = re.search(r"\((.*?)\)", argue_line[1])
            if similar is not None:
                demand = [argue_line[1][:similar.span()[0]], similar.group()[1:-1]]
                if demand[0] in argdict.keys():
                    appel = "{} {}".format(argue_line[0], demand[1])
                    return argdict[demand[0]](appel)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """if true is returned the program will return the closure of program"""
        return True

    def do_EOF(self, arg):
        """the end of program signalled """
        print("")
        return True

    def do_create(self, arg):
        """New class will be created and an instance of id will be created as well
        """
        argue_line = parse(arg)
        if len(argue_line) == 0:
            print("** class name missing **")
        elif argue_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argue_line[0])().id)
            storage.save()

    def do_show(self, arg):
        """shows class and every other instance needed to go through it all
        """
        argue_line = parse(arg)
        object_dictionary = storage.all()
        if len(argue_line) == 0:
            print("** class name missing **")
        elif argue_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argue_line) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argue_line[0], argue_line[1]) not in object_dictionary:
            print("** no instance found **")
        else:
            print(object_dictionary["{}.{}".format(argue_line[0], argue_line[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argue_line = parse(arg)
        object_dictionary = storage.all()
        if len(argue_line) == 0:
            print("** class name missing **")
        elif argue_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argue_line) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argue_line[0], argue_line[1]) not in object_dictionary.keys():
            print("** no instance found **")
        else:
            del object_dictionary["{}.{}".format(argue_line[0], argue_line[1])]
            storage.save()

    def do_all(self, arg):
        """ALL CLASSES TO BE IMPLEMENTED"""
        argue_line = parse(arg)
        if len(argue_line) > 0 and argue_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            object_array = []
            for object_loop in storage.all().values():
                if len(argue_line) > 0 and argue_line[0] == object_loop.__class__.__name__:
                    object_array.append(object_loop.__str__())
                elif len(argue_line) == 0:
                    object_array.append(object_loop.__str__())
            print(object_array)

    def do_count(self, arg):
        """DELETES ALL INSTRANCES UNRELATED TO SUBJECT"""
        argue_line = parse(arg)
        count_number = 0
        for object_loop in storage.all().values():
            if argue_line[0] == object_loop.__class__.__name__:
                count_number += 1
        print(count_number)

    def do_update(self, arg):
        """ A pair of instances to be included in the dictionary
"""

        argue_line = parse(arg)
        object_dictionary = storage.all()

        if len(argue_line) == 0:
            print("** class name missing **")
            return False
        if argue_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argue_line) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argue_line[0], argue_line[1]) not in object_dictionary.keys():
            print("** no instance found **")
            return False
        if len(argue_line) == 2:
            print("** attribute name missing **")
            return False
        if len(argue_line) == 3 and not isinstance(eval(argue_line[2]), dict):
            print("** value missing **")
            return False

        if len(argue_line) == 4:
            object_check = object_dictionary["{}.{}".format(argue_line[0], argue_line[1])]
            if argue_line[2] in object_check.__class__.__dict__.keys():
                value_type = type(object_check.__class__.__dict__[argue_line[2]])
                object_check.__dict__[argue_line[2]] = value_type(argue_line[3])
            else:
                object_check.__dict__[argue_line[2]] = argue_line[3]
        elif isinstance(eval(argue_line[2]), dict):
            object_check = object_dictionary["{}.{}".format(argue_line[0], argue_line[1])]
            for k, v in eval(argue_line[2]).items():
                if (k in object_check.__class__.__dict__.keys() and
                        type(object_check.__class__.__dict__[k]) in {str, int, float}):
                    value_type = type(object_check.__class__.__dict__[k])
                    object_check.__dict__[k] = value_type(v)
                else:
                    object_check.__dict__[k] = v
        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()

