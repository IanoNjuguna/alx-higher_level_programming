#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    new_list = my_list.copy()
    list_length = len(my_list) - 1

    if idx < 0:
        return new_list
    elif idx > list_length:
        return new_list
    else:
        new_list[idx] = element
        return new_list
