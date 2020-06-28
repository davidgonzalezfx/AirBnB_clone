#!/usr/bin/env python3
'''
Console for Airbnb project
'''
import cmd
from datetime import datetime, date
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    ''' Class for Airbnb CLI '''
    prompt = "(hbnb) "

    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
               "Review"]

    def do_quit(self, arg):
        ''' quit command for cmd '''
        return True

    def do_EOF(self, arg):
        ''' EOF command for cmd '''
        print()
        return True

    def emptyline(self):
        ''' Do anything with Enter '''
        pass

    def do_create(self, arg):
        ''' Creates a new instance of BaseModel, saves it in JSON file '''
        if not arg:
            print('** class name missing **')
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except BaseException:
            print("** class doesn't exist **")

    def do_show(self, line):
        ''' Prints the string representation of id instance '''
        args = line.split()
        if not args:
            print('** class name missing **')
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            try:
                key = args[0] + '.' + args[1]
                print(storage.all()[key])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        ''' Deletes an instance based on the class name and id '''
        args = line.split()
        if not args:
            print('** class name missing **')
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            try:
                key = args[0] + '.' + args[1]
                storage.all().pop(key)
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        ''' Prints all string representation of all instances '''
        if not arg:
            my_list = [str(value) for key, value in storage.all().items()]
            if len(my_list) != 0:
                print(my_list)
        elif arg not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            my_list = [str(value) for key,
                       value in storage.all().items() if arg in key]
            if len(my_list) != 0:
                print(my_list)

    def do_update(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif (args[0] not in self.classes):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                key = args[0] + \ '.' + args[1]
                storage.all()[key]
            except KeyError:
                print('** no instance found **')
                return
            if len(args) == 2:
                print("** attribute name missing **")
                return
            elif len(args) == 3:
                print("** value missing **")
                return
            else:
                key = args[0] + \ '.' + args[1]
                try:
                    if '.' in args[3]:
                        value = float(args[3])
                    else:
                        value = int(args[3])
                except ValueError:
                    value = str(args[3]).strip("\"':")
                    value = str(value)
                    setattr(storage.all()[key], args[2].strip("\"':"), value)
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
