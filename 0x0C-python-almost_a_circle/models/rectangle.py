#!/usr/bin/python3
"""create rectangle class"""
from base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter, This will return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter, check if its int"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter, This will return the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter, This will set the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter, This will return the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter, This will set the x and check if x is int"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter, This will return the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter, This will set the y and check if y is int"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
