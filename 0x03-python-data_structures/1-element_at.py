#!/usr/bin/python3
def element_at(my_list, idx):
    listLen = len(my_list) - 1
    if idx < 0 or idx > listLen:
        return (None)
    else:
        return (my_list[idx])
