#!/usr/bin/python3
"""This module is for class Student"""


class Student:
    """This is the class Student"""
    def __init__(self, first_name, last_name, age):
        """This is the init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This is the method to_json"""
        if type(attrs) == list:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """This is the method to_json"""
        self.__dict__ = json
