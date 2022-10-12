#!/usr/bin/python3
""" a class Square that defines a square by: (based on 1-square.py)
Private instance attribute: size
"""


class Square:
    """
     defines a square with private attribute
    """
    def __init__(self, size=0):
        """
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
