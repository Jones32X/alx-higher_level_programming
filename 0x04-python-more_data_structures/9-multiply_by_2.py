#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    N_Dic = a_dictionary.copy()
    for key in N_Dic:
        N_Dic[key] *= 2
    return(N_Dic)
