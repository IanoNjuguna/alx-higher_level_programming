#!/usr/bin/python3
def no_c(my_string):

    for letter in my_string:
        if ord(letter) != ord('c') and ord(letter) != ord('C'):
            print("{}".format(letter), end="")

    return ""
