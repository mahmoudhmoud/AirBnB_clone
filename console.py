#!/usr/bin/env python3
"""
Module
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    the class

    """
    prompt = "(hbnb) "
    my_class = ["BaseModel", "User", "State",
                "City", "Amenity",
                "Place", "Review"]

    def do_create(self, arg):
        """
        arg: class name
        return:  Creates a new instance of BaseModel , saves it
        (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg in self.my_class:
            class_name = arg
            new_instance = globals()[class_name]()
            new_instance.save()
            print(new_instance.id)

        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        return:  all string representation of all instances
        """
        if arg in self.my_class:
            n = []
            for k in storage.all().keys():
                instance = storage.all()[k]
                if instance.__class__.__name__ == arg:
                    n.append(str(instance))
            print(n)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
         Prints the string representation of an instance
         based on the class name and id
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.my_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print('** no instance found **')

    def do_destroy(self, arg):
        """
         Deletes an instance based on the class name and id
         (save the change into the JSON file)
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.my_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print('** no instance found **')

    def do_update(self, arg):
        """ Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.my_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print('** attribute name missing **')
        elif len(args) < 4:
            print('** value missing **')
        elif args[3]:
            key = "{}.{}".format(args[0], args[1])
            va_casted = args[3].replace('"', '')
            if key in storage.all().keys():
                setattr(storage.all()[key], args[2], va_casted)
                storage.save()
            else:
                print('** no instance found **')

    def do_EOF(self, line):
        """Exit command"""
        return True

    do_quit = do_EOF

    def emptyline(self):
        """empty line command"""
        pass

    def default(self, arg):
        if "." in arg:
            commands = arg.strip("()").split('.')
            cls_name, mtd_name = commands[0], commands[1]
            self.do_all(cls_name)
        else:
            return cmd.Cmd.default(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
