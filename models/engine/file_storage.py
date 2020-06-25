#!/usr/bin/env python3
'''
classes:
FileStorage: serialize/deserialize objects to JSON
'''
import json
import os
import uuid
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    ''' FileStorage engine class '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            new_dict = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            json.dump(new_dict, file)

    def reload(self):
        '''Deserializes the JSON file to __objects.'''
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                objs = json.load(file)
                for key, value in objs.items():
                    FileStorage.__objects[key] = eval(
                        value['__class__'])(**value)
