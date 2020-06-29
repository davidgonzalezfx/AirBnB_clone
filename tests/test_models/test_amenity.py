#!/usr/bin/python3
"""Test Amenity"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class TestAmenity(unittest.TestCase):
    """Test Amenity file"""

    def test_class(self):
        """Test the class."""
        amenity1 = Amenity()
        self.assertEqual(amenity1.__class__.__name__, "Amenity")

    def test_father(self):
        """Test the class."""
        amenity1 = Amenity()
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))

    def test_amenity(self):
        """Test attributes of the class."""
        my_amenity = Amenity()
        my_amenity.name = "Wi-Fi"
        self.assertEqual(my_amenity.name, 'Wi-Fi')

    def test_type(self):
        """Test amenity value type."""
        amenity1 = Amenity()
        self.assertEqual(type(amenity1.name), str)
        self.assertNotEqual(type(amenity1.name), list)

    def test_attribute(self):
        """Test another attributes."""
        amenity1 = Amenity()
        self.assertTrue(hasattr(amenity1, "name"))
        self.assertFalse(hasattr(amenity1, "area"))
