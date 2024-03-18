#!/usr/bin/python3
def no_c(my_string):
    charsLst = list(my_string)
    for CharacterC in charsLst:
        if CharacterC == 'c' or CharacterC == 'C':
            charsLst.remove(CharacterC)
            return("".join(charsLst))
