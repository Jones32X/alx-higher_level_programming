#!/usr/bin/python3
for x in range(0, 10):
    for p in range(1, 10):
        if x >= p:
            continue
        elif x == 8 and p == 9:
            print("{}{}".format(x, p))
        else:
            print("{}{}, ".format(x, p), end="")
