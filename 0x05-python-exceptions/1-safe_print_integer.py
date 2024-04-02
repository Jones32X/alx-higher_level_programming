#!/usr/bin/python3

def safe_print_list(value):
    cnt = 0

    for me in range(x):
        try:
            print("{}".format(my_list[me]), end="")
            cnt += cnt + 1
        except IndexError:
            continue
    print("")
    return cnt
