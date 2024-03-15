#!/usr/bin/python3
def remove_char_at(str, n):
    newStr = ""
    for j in range(len(str)):
        if j == n:
            continue
        else:
            newStr += str[j]
    return newStr
