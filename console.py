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


class HBNBCommand(cmd.Cmd):
    """implementation of class"""
    prompt = '(hbnb) '
    defined_class_list = ["BaseModel", "User", "State",
                          "City", "Amenity", "Place",
                          "Review"
                          ]

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
