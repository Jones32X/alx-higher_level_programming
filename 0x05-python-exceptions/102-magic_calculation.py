#!/usr/bin/python3

def magic_calculation(a, b):

    res = 0

    for me in range(1, 3):
        try:
            if me > a:
                raise Exception("Too far")
            res = res + (a ** b) / me
        except Exception:
            res = b + a
            break
    return res
