#!/usr/bin/python3
"""AirBnB command interpreter"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User


def parser(arg):
    c_braces = re.search(r"\{(.*?)\}", arg)
    parenthesis = re.search(r"\[(.*?)\]", arg)
    if c_braces is None:
        if parenthesis is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lex = split(arg[:paranthesis.span()[0]])
            rtl = [i.strip(",") for i in lex]
            rtl.append(parenthesis.group())
            return rtl
    else:
        lex = split(arg[:c_braces.span()[0]])
        rtl = [i.strip(",") for i in lex]
        rtl.append(c_braces.group())
        return rtl


class HBNBCommand(cmd.Cmd):
    """implements the command interpreter class"""
    prompt = "(hbnb) "
    __classes = {
            "BaseModel"
            }

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """creates a new instance of the BaseModel class,
        saves it and prints th id
        """
        args = parser(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = parser(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = parser(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_update(self, arg):
        """Updates a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        args = parser(arg)
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = obj_dict["{}.{}".format(argl[0], argl[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = obj_dict["{}.{}".format(argl[0], argl[1])]
            od = obj.__class__.__dict__
            for key, val in eval(args[2]).items():
                if (key in od.keys() and
                        type(od[key]) in {str, int, float}):
                    valtype = type(od[key])
                    obj.__dict__[key] = valtype(val)
                else:
                    obj.__dict__[key] = val
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        """
        args = parser(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(args) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_quit(self, arg):
        """Quits the program"""
        return True

    def do_EOF(Self, arg):
        """ EOF signal to quit the  program"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
