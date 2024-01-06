#!/usr/bin/python3
""" initializing class ."""
class Square:
    """ initializing new object"""
    def __init__(self, size = 0):
        """ consrructor 
        Args:
        size = the size of the square
        Raise:
        TypeError: if the size is not integer
        ValueError: if the size < 0 .
        """
        if not isinstance(size, int):
            raise TypeError(' size must be an integer ')
       elif size < 0:
            raise ValueError(' size must be >= 0 ')
        self.__size = size
                                
