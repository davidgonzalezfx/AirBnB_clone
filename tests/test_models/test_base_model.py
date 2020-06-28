#!/usr/bin/python3
'''
Test: BaseModel
'''

import io
import unittest
import unittest.mock
from models.base_model import BaseModel
from datetime import datetime


class test_base_model(unittest.TestCase):
    ''' Test class for base_model '''

    def tearDown(self):
        ''' After tests, remove json file '''
        try:
            remove("file.json")
        except Exception:
            pass

    def test_empty_constructor(self):
        ''' Create object without args/kwargs '''
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(type(obj.id), str)
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(type(obj.created_at), datetime)
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertTrue(type(obj.updated_at), datetime)

    def test_kwargs_constructor(self):
        ''' Create object passing Kwargs '''
        dictonary = {'id': 'cc9909cf-a909-9b90-9999-999fd99ca9a9',
                     'created_at': '2025-06-28T14:00:00.000001',
                     '__class__': 'BaseModel',
                     'updated_at': '2030-06-28T14:00:00.000001',
                     'score': 100
                     }

        obj = BaseModel(**dictonary)
        self.assertTrue(hasattr(obj, "__class__"))
        self.assertFalse(obj.__class__ == 'BaseModel')

        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertTrue(hasattr(obj, 'score'))

        self.assertTrue(type(obj.created_at), datetime)
        self.assertTrue(type(obj.updated_at), datetime)

        self.assertEqual(obj.id, 'cc9909cf-a909-9b90-9999-999fd99ca9a9')
        self.assertEqual(
            obj.created_at.isoformat(),
            '2025-06-28T14:00:00.000001')
        self.assertEqual(
            obj.updated_at.isoformat(),
            '2030-06-28T14:00:00.000001')
        self.assertEqual(obj.score, 100)

    def test_kwargs_constructor_2(self):
        ''' Create object passing Kwargs, without id and dates '''
        dictonary = {'score': 100}

        obj = BaseModel(**dictonary)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertTrue(hasattr(obj, 'score'))

    def test_empty_constructor_ids(self):
        ''' Test id generator '''
        obj = BaseModel()
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertTrue(obj.id != obj1.id)
        self.assertTrue(obj.id != obj2.id)
        self.assertTrue(obj1.id != obj2.id)

    def test_str_method(self):
        ''' Test str method '''
        dictonary = {'id': 'cc9909cf-a909-9b90-9999-999fd99ca9a9',
                     'created_at': '2025-06-28T14:00:00.000001',
                     '__class__': 'BaseModel',
                     'updated_at': '2030-06-28T14:00:00.000001',
                     'score': 100
                     }

        obj = BaseModel(**dictonary)
        out = "[{}] ({}) {}\n".format(type(obj).__name__, obj.id, obj.__dict__)

        @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
        def assert_stdout(self, expected_output, mock_stdout):
            print(obj)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        def test_str(self):
            self.assert_stdout(out)

    def test_save_method(self):
        ''' Test save method '''
        obj = BaseModel()
        created = obj.created_at
        updated = obj.updated_at
        obj.save()
        self.assertTrue(created == obj.created_at)
        self.assertTrue(updated != obj.updated_at)

    def test_to_dict_method(self):
        ''' Test to_dict method '''
        obj = BaseModel(score=100)
        new_dict = obj.to_dict()

        self.assertEqual(new_dict['id'], obj.id)
        self.assertEqual(new_dict['score'], 100)
        self.assertEqual(new_dict['__class__'], 'BaseModel')
        self.assertEqual(new_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(new_dict['updated_at'], obj.updated_at.isoformat())

        self.assertEqual(type(new_dict['created_at']), str)
        self.assertEqual(type(new_dict['created_at']), str)
