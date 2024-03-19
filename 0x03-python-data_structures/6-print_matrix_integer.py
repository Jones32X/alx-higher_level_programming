#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for v in matrix:
        T = 1
        for b in v:
            if T == len(v):
                print("{:d}".format(b), end="")
            else:
                print("{:d}".format(b), end=" ")
            T = T + 1
        print()
