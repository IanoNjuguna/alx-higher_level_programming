#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for column in row:
            end_list = row[-1]

            print("{:d}".format(column), end="")

            if column != end_list:
                print(end=" ")
            elif column == None:
                print()
            else:
                print("\n", end="")
