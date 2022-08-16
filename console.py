#!/usr/bin/python3
"""
This is the console necessary for the project
This is a commnent
"""

import cmd
import os

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

