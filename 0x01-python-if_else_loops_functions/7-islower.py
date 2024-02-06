#!/usr/bin/python3

def islower(c):
    lower_a = ord("a")
    lower_z = ord("z")

    if ord(c) >= lower_a and ord(c) <= lower_z:
        return True
    else:
        return False
