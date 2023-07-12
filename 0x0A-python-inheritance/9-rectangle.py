#!/usr/bin/python3
"""import base_geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        """Initialize Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """function area"""
        return self.__width * self.__height

    def __str__(self):
        """string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
