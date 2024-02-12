#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    list_length = len(my_list) - 1

    if idx < 0:
        return my_list
    elif idx > list_length:
        return my_list
    else:
        my_list[idx] = element
        return my_list
