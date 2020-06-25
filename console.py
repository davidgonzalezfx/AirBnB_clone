#!/usr/bin/env python3
'''
Console for Airbnb project
'''
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    ''' Class for Airbnb CLI '''
    prompt = "(hbnb) "

    def do_prompt(self, line):
        '''Print the line.'''
        print('{} , {}'.format(self.prompt, line))

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


if __name__ == '__main___':
    HBNBCommand().cmdloop()
