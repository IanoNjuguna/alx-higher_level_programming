#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not isinstance(my_list, list):
        return 1
    else:
        my_list.reverse()

        for item in my_list:
            print("{:d}".format(item))
