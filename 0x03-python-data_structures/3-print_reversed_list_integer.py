#!/bin/usr/python3
def print_reversed_list_integer(my_list=[]):
    for rev in (my_list[::-1]):
        print("{:d}".format(rev))
