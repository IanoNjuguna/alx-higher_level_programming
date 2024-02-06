#!/usr/bin/python3

def print_last_digit(number):

    last_number = abs(number) % 10

    print("{}".format(last_number), end="")

    return last_number
