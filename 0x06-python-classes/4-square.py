#!/usr/bin/pyrhin3
class square:
    """ defining a class """

    def __init__(self, size = 0):
        """ initializing anew object 
        Args: size > the long of one side from a square 
        Raise: ValueError if the size is < 0
        Raise: TypeError if the size is not an integer .
        """
        @property
            def size(self):
                return self.__size
        @size.setter
        def (self, value):
            if not isinstance(value, int):
                raise TypeError('size must be an integer')
            elif value < 0 :
                raise ValueError(' size must be >= 0 ')
            self.__size = size

            def area(self):
                return self.__size ** 2

