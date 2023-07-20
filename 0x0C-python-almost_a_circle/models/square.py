#!/usr/bin/python3
from rectangle import Rectangle
"""Import Rectangle"""


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get width and height"""
        return self.width

    @size.setter
    def size(self, value):
        """Set width and height"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square"""
        if len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
