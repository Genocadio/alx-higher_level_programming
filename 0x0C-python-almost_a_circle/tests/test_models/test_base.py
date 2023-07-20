#!/usr/bin/python3
import unittest
from models.base import Base
"""Test Base class"""


class TestBase(unittest.TestCase):
    """Test Base class"""
    def test_with_provided_id(self):
        obj1 = Base(11)
        self.assertEqual(obj1.id, 11)

    def test_without_provided_id(self):
        """Test without provided id"""
        obj2 = Base()
        obj3 = Base()
        obj4 = Base()
        self.assertEqual(obj2.id, 3)
        self.assertEqual(obj3.id, 4)
        self.assertEqual(obj4.id, 5)

    def test_with_multiple_provided_ids(self):
        """Test with multiple provided ids"""
        obj5 = Base(30)
        obj6 = Base(220)
        obj7 = Base(31)
        self.assertEqual(obj5.id, 30)
        self.assertEqual(obj6.id, 220)
        self.assertEqual(obj7.id, 31)

    def test_mix_of_provided_and_non_provided_ids(self):
        """Test mix of provided and non provided ids"""
        obj8 = Base()
        obj9 = Base(550)
        obj10 = Base()
        self.assertEqual(obj8.id, 1)
        self.assertEqual(obj9.id, 550)
        self.assertEqual(obj10.id, 2)

    def test_to_json_string(self):
        """Test converting a list of dictionaries to JSON"""
        list_dicts = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        json_string = Base.to_json_string(list_dicts)
        expcted_json = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(json_string, expcted_json)

        """Test converting an empty list to JSON"""
        empty_list = []
        json_string = Base.to_json_string(empty_list)
        expected_json = '[]'
        self.assertEqual(json_string, expected_json)

    def test_from_json_string(self):
        """Test converting JSON to a list of dictionaries"""
        json_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        list_dicts = Base.from_json_string(json_string)
        expected_list = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        self.assertEqual(list_dicts, expected_list)

        """Test converting an empty JSON to an empty list"""
        empty_json = '[]'
        list_dicts = Base.from_json_string(empty_json)
        expected_list = []
        self.assertEqual(list_dicts, expected_list)


if __name__ == "__main__":
    """Run tests"""
    unittest.main()
