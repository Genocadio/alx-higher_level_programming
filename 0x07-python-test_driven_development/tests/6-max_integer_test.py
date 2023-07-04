#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class MaxIntegerTestCase(unittest.TestCase):
    def test_empty_list(self):
        """Test for an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        """Test for a list with a single element"""
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        """Test for a list of positive numbers"""
        result = max_integer([1, 3, 2, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """Test for a list of negative numbers"""
        result = max_integer([-1, -3, -2, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test for a list of mixed positive and negative numbers"""
        result = max_integer([-1, 3, -2, 4, -5])
        self.assertEqual(result, 4)

    def test_duplicate_numbers(self):
        """Test for a list with duplicate numbers"""
        result = max_integer([5, 5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_float_numbers(self):
        """Test for a list of floating-point numbers"""
        result = max_integer([1.5, 2.7, 3.2, 2.1])
        self.assertEqual(result, 3.2)

    def test_invalid_input(self):
        """Test for invalid input"""
        with self.assertRaises(TypeError):
            max_integer(123)

if __name__ == '__main__':
    unittest.main()
