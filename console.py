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

    do_quit(self):
        """
        Quit cmd to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop("(hbnb)")
