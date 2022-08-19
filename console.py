#!/usr/bin/python3
"""
This is the console necessary for the project
This is a commnent
"""

import cmd
import json
import os

from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This is my console class
    """

    prompt = '(hbnb) '

    def emptyline(self):
        """
        Do nothing when no command entered
        """
        pass

    def do_quit(self, s):
        """
        Quits the program
        """
        return True

    def help_quit(self):
        """
        documantation for quit
        """
        print("Quit command to exit the program")

    do_EOF = do_quit
    help_EOF = help_quit

    def do_create(self, arg):
        """
        Creates a new user
        """
        if arg == "BaseModel":
            newuser = BaseModel()
            newuser.save()
            print(newuser.id)
        elif arg == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        show a class intance and print string representation
        """
        storage.reload()
        objdict = storage.all()
        if arg == "":
            print("** class name missing **")
        else:
            splitted = arg.split()
            if len(splitted) == 1:
                print("** instance id missing **")
                return
            if splitted[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            basekey = "{}.{}".format(splitted[0], splitted[1])
            if basekey not in objdict:
                print("** no instance found **")
                return
            olduser = BaseModel(objdict[basekey])
            print(olduser)

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name
        """
        storage.reload()
        objdict = storage.all()
        if arg == "":
            print("** class name missing **")
        else:
            splitted = arg.split()
            if len(splitted) == 1:
                print("** instance id missing **")
                return
            if splitted[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            basekey = "{}.{}".format(splitted[0], splitted[1])
            if basekey not in objdict:
                print("** no instance found **")
            else:
                del objdict[basekey]
            with open("file.json", "w") as file:
                json.dump(objdict, file)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
