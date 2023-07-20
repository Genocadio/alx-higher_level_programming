#!/usr/bin/python3
import unittest
from models.base import Base
"""Test Base class"""


class TestBase(unittest.TestCase):
    """Test Base class"""
    def test_with_provided_id(self):
        obj1 = Base(10)
        self.assertEqual(obj1.id, 10)

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
        obj5 = Base(100)
        obj6 = Base(200)
        obj7 = Base(300)
        self.assertEqual(obj5.id, 100)
        self.assertEqual(obj6.id, 200)
        self.assertEqual(obj7.id, 300)

    def test_mix_of_provided_and_non_provided_ids(self):
        """Test mix of provided and non provided ids"""
        obj8 = Base()
        obj9 = Base(500)
        obj10 = Base()
        self.assertEqual(obj8.id, 1)
        self.assertEqual(obj9.id, 500)
        self.assertEqual(obj10.id, 2)

    def test_to_json_string(self):
        """Test converting a list of dictionaries to JSON"""
        list_dicts = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        json_string = Base.to_json_string(list_dicts)
        expcted_json = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        self.assertEqual(json_string, expcted_json)

        """Test converting an empty list to JSON"""
        empty_list = []
        json_string = Base.to_json_string(empty_list)
        expected_json = '[]'
        self.assertEqual(json_string, expected_json)

    def test_from_json_string(self):
        """Test converting JSON to a list of dictionaries"""
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        list_dicts = Base.from_json_string(json_string)
        expected_list = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        self.assertEqual(list_dicts, expected_list)

        """Test converting an empty JSON to an empty list"""
        empty_json = '[]'
        list_dicts = Base.from_json_string(empty_json)
        expected_list = []
        self.assertEqual(list_dicts, expected_list)


if __name__ == "__main__":
    """Run tests"""
    unittest.main()
