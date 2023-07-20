#!/usr/bin/python3
"""Test Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""

    def test_constructor(self):
        """Test constructor"""
        rect = Rectangle(4, 11, 21, 13, 21)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 11)
        self.assertEqual(rect.x, 21)
        self.assertEqual(rect.y, 13)
        self.assertEqual(rect.id, 21)

    def test_area(self):
        """Test area"""
        rect = Rectangle(4, 11)
        self.assertEqual(rect.area(), 44)

    def test_string_representation(self):
        """Test string representation"""
        rect = Rectangle(5, 14, 8, 6, 2)
        self.assertEqual(str(rect), "[Rectangle] (2) 8/6 - 5/14")

    def test_update(self):
        """Test update"""
        rect = Rectangle(1, 14, 32, 4, 2)
        rect.update(4, 10, 14, 57, 8)
        self.assertEqual(rect.id, 4)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 14)
        self.assertEqual(rect.x, 57)
        self.assertEqual(rect.y, 8)

        rect.update(height=25, x=8)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 8)

    def test_to_dictionary(self):
        """Test to_dictionary"""
        rect = Rectangle(53, 210, 32, 34, 121)
        expcted_dict = {
            "id": 121,
            "width": 53,
            "height": 210,
            "x": 32,
            "y": 34
        }
        self.assertEqual(rect.to_dictionary(), expcted_dict)


if __name__ == "__main__":
    """main"""
    unittest.main()
