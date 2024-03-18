#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for v in matrix:
        K = 1
        for x in v:
            if K == len(v):
                print("{:d}".format(x), end="")
            else:
                print("{:d}".format(x), end=" ")
                K += 1
                print()
