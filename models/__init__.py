#!/usr/bin/env python3
'''
Module that creates just one instance of FileStorage
'''
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
