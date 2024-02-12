#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list_length = len(my_list) - 1

    for item in range(list_length, -1, -1):
        print("{:d}".format(my_list[item]))
