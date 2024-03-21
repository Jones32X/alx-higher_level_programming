#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    digit = 0
    DAN = 0

    for tup in my_list:
        digit = digit + tup[0] * tup[1]
        DAN = DAN + tup[1]

    return (digit / DAN)
