#!/usr/bin/python3
"""This module contains the HBNBCommand class which is the entry point of the command interpreter."""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB console."""
    prompt = "(hbnb)"

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)."""
        print()
        return True

    def help_quit(self):
        """Print help message for the quit command."""
        print("Exit the program.")

    def help_EOF(self):
        """Print help message for the EOF command."""
        print("Exit the program using EOF (Ctrl+D).")

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it and print the id."""
        if not arg:
            print("** class name missing **")
        elif arg not in globals():
                print("** class doesn't exist **")
        else:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** nor instance found **")

    def do_all(self, arg):
        """Prints string representation of all instances."""
        args = arg.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        elif args[0] not in globals():
            print("** class doesn't exist **")
            return
        else:
            for key, obj in storage.all().items():
                if key.split('.')[0] == args[0]:
                    obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                setattr(obj, args[2], args[3].strip('"'))
                obj.save()
                
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
