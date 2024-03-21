#!/usr/bin/python3
def to_subtract(list_num):
    to_SUBS = 0
    maximum_list = max(list_num)

    for n in list_num:
        if maximum_list > n:
            to_SUBS = + n

    return (maximum_list - to_SUBS)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    number = 0
    last_roman_N = 0
    list_number_N = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_n.get(ch) <=  last_roman_N:
                    number += to_subtract(list_number_N)
                    list_number_N = [rom_n.get(ch)]
                else:
                    list_number_N.append(rom_n.get(ch))

                last_roman_N = rom_n.get(ch)

    number = number + to_subtract(list_number_N)

    return (number)
