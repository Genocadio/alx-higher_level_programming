#!/usr/bin/python3
"""create rectangle class"""
from base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the class Rectangle
        it inherits from Base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width getter
        This will return the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        This will set the width and check if width is int
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        This will return the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        This will set the height and check if height is int
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x getter
        This will return the x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        This will set the x and check if x is int
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y getter
        This will return the y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        This will set the y and check if y is int
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        This uses width and height to calculate the area
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        This will print the rectangle
        Prints the rectangle with the character #
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        This converts the rectangle to a string
        Returns the string representation of the rectangle
        """
        hei = self.height
        r = f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{hei}"
        return r

    def update(self, *args, **kwargs):
        """
        alguments:
        args: list of attributes to set
        kwargs: dictionary of attributes to set
        Updates the public instance attributes
        """
        if len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        It converts the rectangle to a dictionary
        Returns the dictionary representation of the rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
