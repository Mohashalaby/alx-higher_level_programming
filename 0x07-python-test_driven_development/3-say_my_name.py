#!/usr/bin/python3
"""Define function that say my name """
def say_my_name(first_name, last_name=""):
    """Arguments:
    strings last & first name>
    Raises : Typeerror if two arguments not string>
    first name must be astring or last name must be astring"""
    if not (isinstance(first_name, str):
            raise TypeError("first_name must be a string")
            if not (isinstance(last_name, str):
                raise TypeError("last_name must be a string")
                print("My name is {} {}".format(first_name, last_name))
