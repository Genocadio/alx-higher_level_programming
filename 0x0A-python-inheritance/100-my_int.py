#!/usr/bin/python3
"""module for class MyList"""


class MyInt(int):
    """Class MyInt"""
    def __eq__(self, other):
        """override __eq__"""
        return False

    def __ne__(self, other):
        """override __ne__"""
        return True
