#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0) :
    """Initialize a new Square.

    Args:
    size (int): The size of the new square

    Raise:
    typeError if the size not integer.
    valueErrot if the size less than 0..
    """

    if not isinstance(size, int) :
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    self.__size = size

