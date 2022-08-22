#!/usr/bin/python3
"""
This is the console necessary for the project
This is a commnent
I reaaly do not understand documentation again
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
            if splitted[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            if len(splitted) == 1:
                print("** instance id missing **")
                return
            basekey = "{}.{}".format(splitted[0], splitted[1])
            if basekey not in objdict:
                print("** no instance found **")
                return
            olduser = BaseModel(**objdict[basekey])
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
            if splitted[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            if len(splitted) == 1:
                print("** instance id missing **")
                return
            basekey = "{}.{}".format(splitted[0], splitted[1])
            if basekey not in objdict:
                print("** no instance found **")
            else:
                del objdict[basekey]
            with open("file.json", "w") as file:
                json.dump(objdict, file)

    def do_all(self, arg):
        """
        prints a list of string representation of all instance
        if a class name is specified, all instance of the class is printed.
        """
        storage.reload()
        instances = storage.all()
        classes = []
        for key in instances.keys():
            inst = BaseModel(**instances[key])
            if arg == "":
                classes.append(str(inst))
            elif inst.__class__.__name__ == arg:
                classes.append(str(inst))
        if len(classes) == 0:
            print("** class doesn't exist **")
        else:
            print(classes)

    def do_update(self, arg):
        """
        From here we try to update certain atrributes,
        one at a time
        """
        storage.reload()
        objdict = storage.all()
        if arg == "":
            print("** class name missing **")
        else:
            splitted = arg.split()
            if splitted[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            if len(splitted) == 1:
                print("** instance id missing **")
                return
            basekey = "{}.{}".format(splitted[0], splitted[1])
            if basekey not in objdict:
                print("** no instance found **")
                return
            if len(splitted) == 2:
                print("** attribute name missing **")
                return
            attrlist = objdict.get(basekey)
            if splitted[2] not in attrlist:
                print("** value missing **")
                return
            #updtstr = "{}={}".format(splitted[2], splitted[3])
            attrlist.update({splitted[2]:splitted[3]})
            dictupdt = {basekey:attrlist}
            objdict.update(dictupdt)
            with open("file.json", "w") as file:
                json.dump(objdict, file)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
