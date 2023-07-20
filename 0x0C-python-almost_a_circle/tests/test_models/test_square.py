#!/usr/bin/python3
"""Test square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square class"""

    def test_constructor(self):
        """Test constructor"""
        square = Square(6, 4, 9, 3)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 9)
        self.assertEqual(square.id, 3)

    def test_area(self):
        """Test area"""
        square = Square(4)
        self.assertEqual(square.area(), 16)

    def test_string_representation(self):
        """Test string representation"""
        square = Square(8, 6, 5, 4)
        self.assertEqual(str(square), "[Square] (4) 6/5 - 8")

    def test_update(self):
        """Test update"""
        square = Square(1, 24, 33, 14)
        square.update(4, 13, 6, 7)
        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 13)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 7)

        square.update(size=18, y=9)
        self.assertEqual(square.size, 18)
        self.assertEqual(square.y, 9)

    def test_to_dictionary(self):
        """Test to_dictionary"""
        square = Square(8, 4, 9, 3)
        expcted_dict = {
            "id": 3,
            "size": 8,
            "x": 4,
            "y": 9
        }
        self.assertEqual(square.to_dictionary(), expcted_dict)


if __name__ == "__main__":
    """main"""
    unittest.main()
