#!/usr/bin/python3
"""
This is a module that writes a class
Square that defines a square by: (based on 0-square.py)
"""
class Square:
    """Function that defines a square"""
    def __init__(self, size):
        self.__size = size
        """
        Private instance attribute: size
        Instatation with size
        (no type/value verification)
        """
