#!/usr/bin/python3
"""AirBnB console"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
    """implements the command interpreter class

    Attributes:
        prompt (str): The prompt
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
        """Do nothing on empty line"""
        pass

    def default(self, arg):
        """defines actions for cmd module when input is invalid"""
        args_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_l = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_l[1])
            if match is not None:
                command = [arg_l[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in args_dict.keys():
                    call = "{} {}".format(arg_l[0], command[1])
                    return args_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

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

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieves the number of instances of a given class.
        """
        args = parser(arg)
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

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
