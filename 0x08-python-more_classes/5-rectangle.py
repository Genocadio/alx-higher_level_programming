#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Defines a class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle attributes."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns the printable representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ['#'] * self.__width + ['\n']
        rect = rect * (self.__height - 1) + ['#'] * self.__width
        return ''.join(rect)

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message for each deletion"""
        print("Bye rectangle...")
