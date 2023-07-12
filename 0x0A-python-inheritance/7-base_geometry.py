#!/usr/bin/python3
"""Module for class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """function area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

bg = BaseGeometry()
print(dir(bg))