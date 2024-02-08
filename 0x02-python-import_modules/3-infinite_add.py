#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    len_argv = len(argv)
    argc = len_argv - 1
    count = 0

    for len_argv in range(0, argc):
        count += int(argv[len_argv + 1])

    print(count)
