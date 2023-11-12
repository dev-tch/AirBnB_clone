#!/usr/bin/python3
"""entry point of the command interpreter"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import cmd
import shlex
import re
import sys


class HBNBCommand(cmd.Cmd):
    """implementation of class"""
    prompt = '(hbnb) '
    defined_class_list = ["BaseModel", "User", "State",
                          "City", "Amenity", "Place",
                          "Review"
                          ]
    custom_procs = ["all", "count", "show", "destroy", "update"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_EOF(self, line):
        """EOF signal to exit the program"""
        return True

    def do_help(self, arg):
        """Display help message"""
        super().do_help(arg)

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.defined_class_list:
            print("** class doesn't exist **")
        else:
            # create instance from argument command
            new_object = eval(arg)()
            # save object to JSON file
            new_object.save()
            # print id attribute of object
            print(new_object.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.defined_class_list:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            str_object_id = ".".join(map(str, args[:2]))
            # search in storage __objects for this id "
            ref_obj_found = storage.all().get(str_object_id, None)
            if ref_obj_found is None:
                print("** no instance found **")
            else:
                print(ref_obj_found)

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.defined_class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            str_object_id = ".".join(map(str, args[:2]))
            # search in storage __objects for this id
            ref_removed_obj = storage.all().pop(str_object_id, None)
            if ref_removed_obj is None:
                print("** no instance found **")
            else:
                storage.save()

    def do_all(self, arg):
        """Print all string representation of all instances"""
        args = shlex.split(arg)
        if not args:
            # show all instances in storageFile
            str_obj_list = [str(ref_obj) for ref_obj in storage.all().values()]
            print(str_obj_list)
        elif args[0] not in HBNBCommand.defined_class_list:
            print("** class doesn't exist **")
        else:
            # show all instances of a custom class Name
            str_obj_list = [str(ref_obj) for ref_obj in storage.all().values()
                            if type(ref_obj).__name__ == args[0]]
            print(str_obj_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.defined_class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            str_object_id = ".".join(map(str, args[:2]))
            # search in storage __objects for this id
            ref_obj_found = storage.all().get(str_object_id, None)
            if ref_obj_found is None:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj_attr_name = args[2]
                obj_attr_val = args[3]

                try:
                    # convert attribute value to correct type
                    if hasattr(ref_obj_found, obj_attr_name):
                        attr_value_type = type(getattr(ref_obj_found,
                                                       obj_attr_name))
                    else:
                        # if the attribute doesn't exist
                        attr_value_type = type(obj_attr_val)

                    casted_attr_obj_val = attr_value_type(obj_attr_val)

                    # update object new attribute
                    setattr(ref_obj_found, obj_attr_name, casted_attr_obj_val)
                    # save object to file storage after successful update
                    ref_obj_found.save()
                except ValueError:
                    pass

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.defined_class_list:
            print("** class doesn't exist **")
        else:
            # count instances of the specified class
            count = sum(1 for obj in storage.all().values()
                        if type(obj).__name__ == args[0])
            print(count)

    def default(self, args):
        """ execute custom command"""
        # init local variables
        name_cls = ""
        name_proc = ""
        params = ""
        method_name = ""
        flag = True
        # regex to extract elements of method
        data = re.findall(r"(\w+)\.(\w+)\((.*?)\)", args)
        if data:
            name_cls = data[0][0]
            name_proc = data[0][1]
            params = data[0][2]
        if params and name_proc in HBNBCommand.custom_procs[0:2]:
            flag = False
        elif name_proc in HBNBCommand.custom_procs[2:4]:
            if not re.match(r"\"[a-zA-Z0-9-]+\"", params):
                flag = False
        elif name_proc == HBNBCommand.custom_procs[4]:
            # <id>, <attribute name>, <attribute value>
            reg1 = r"\"[a-zA-Z0-9-]+\", \"\w+\", \"\w+\""
            # <id>, <dictionary representation>
            reg2 = r"\"[a-zA-Z0-9-]+\", {.*}"
            reg1_ok = False
            reg2_ok = False
            if re.match(reg1, params):
                reg1_ok = True
                params = params.replace(",", " ")
            elif re.match(reg2, params):
                reg2_ok = True
                params = params.replace(",", " ", 1)
            if not reg1_ok and not reg2_ok:
                flag = False
        if (flag and name_cls in HBNBCommand.defined_class_list and
                name_proc in HBNBCommand.custom_procs):
            method_name = "do_{}".format(name_proc)
            if (hasattr(self, method_name) and
                    callable(getattr(self, method_name))):
                method = getattr(self, method_name)
                return method(f"{name_cls} {params}")
        print("*** Unknown syntax: {}".format(args))
        return False

    def preloop(self):
        """handle non-interactive mode"""
        if not sys.stdin.isatty():
            self.prompt = self.prompt + "\n"


if __name__ == '__main__':
    my_console = HBNBCommand()
    if len(sys.argv) > 1:
        my_console.onecmd(' '.join(sys.argv[1:]))
    else:
        my_console.cmdloop()
