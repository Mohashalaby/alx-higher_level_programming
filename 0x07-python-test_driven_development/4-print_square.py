#!/usr/bin/python3
"""define a function that print asquare"""
def print_square(size):
    """
    Args:
    size: is the size lengh of the square.
    Raise:
    typeerror : if the size is not integer.
    ValueError : if the size is less than 0.
    TypeError: if size is afloat and less than 0.
    """
    if not(isinstance(size, int):
            raise TypeError("size must be an integer")
            if size < 0:
            raise ValueError(" size must be >= 0")
            if (isinstance(size, float) and size < 0:
                raise TypeError("size must be an integer")
                for i in range (size):
                [print("#", end=" ") for j in range(size)]
                print("")
