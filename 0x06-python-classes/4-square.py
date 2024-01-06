#!/usr/bin/pyrhin3
"""define a class square """


class Square:
"""rebresent a square"""

    def __init__(self, size = 0):
        """ initializing anew object 
        Args: size > the long of one side from a square 
        Raise: ValueError if the size is < 0
        Raise: TypeError if the size is not an integer .
        """

        @property
            def size(self):
                """ get/set the current size of the square """

                return self.__size
        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError('size must be an integer')
            elif value < 0 :
                raise ValueError('size must be >= 0')
            self.__size = value

            def area(self):
                " return the  current area of the square"""
                return self.__size ** 2

