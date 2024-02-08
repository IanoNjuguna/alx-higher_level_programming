#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    len_argv = len(argv)
    argc = len_argv - 1

    if argc != 0 and argc != 1:
        print("{:d} arguments:".format(argc))
    elif argc == 0:
        print("{:d} arguments.".format(argc))
    else:
        print("{:d} argument:".format(argc))

    for len_argv in range(0, argc):
        print("{:d}: {}".format((len_argv + 1), argv[len_argv + 1]))
