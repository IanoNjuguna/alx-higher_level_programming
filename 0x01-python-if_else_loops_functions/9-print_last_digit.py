#!/usr/bin/python3

def print_last_digit(number):
    last_number = number % 10

    print(f"{last_number:02d}", end = "")
