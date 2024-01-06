#!/usr/bin/python3
"""defining a class . """

class Square:
    """implement a class """
    def __init__(self, size = 0):

    """ constructor 
    Args: (int) size = the size of asquare .
    Raise:
     TypeError: if the size is not integer.
     ValueError: if the size is < 0.
     """

     if not isinstance(size, int):
         raise TypeError('size must be an integer')
     elif size < 0 :
         raise ValueError('size must be >= 0')
     self.__size = size

     def area(self):
         """ return thr current area of the square"""
         return self.__size **2
