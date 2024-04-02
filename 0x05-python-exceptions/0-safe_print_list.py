#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    L = 0
    prints = 0
    for L in range(0, x):
        try:
            print("{}".format(my_list[L]), end="")
            prints = prints + 1
        except IndexError:
            continue
    print()
    return prints
