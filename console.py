#!/usr/bin/python3
"""AirBnB command interpreter"""
import cmd


clas HBNBCommand(cmd.Cmd):
    """implements the command interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quits the program"""
        return True

    def do_EOF(Self, arg):
        """ EOF signal to quit the  program"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
