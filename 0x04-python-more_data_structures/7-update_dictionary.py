#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    N_Dicti = a_dictionary.copy()
    for key in N_Dicti:
         N_Dicti[key] *= 2
    return(N_Dicti)
