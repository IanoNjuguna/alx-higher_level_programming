#!/usr/bin/python3

for number in range(0, 100):
    if number < 10:
        print(0, end="")

    print(f"{number:d}", end="")

    if number != 99:
        print(", ", end="")
    else:
        print("\n")
