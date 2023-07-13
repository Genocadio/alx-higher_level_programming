#!/usr/bin/python3
"""This module is for class Student"""


class Student:
    """This is the class Student"""
    def __init__(self, first_name, last_name, age):
        """This is the init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This is the method to_json"""
        return self.__dict__
