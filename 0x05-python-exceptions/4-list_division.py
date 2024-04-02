#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    count = 0
    K = 0
    L_list = []

    for K in range(list_length):
        try:
            res = my_list_1[K] / my_list_2[K]
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            L_list.append(res)
    return L_list
