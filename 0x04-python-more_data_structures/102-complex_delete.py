def complex_delete(a_dictionary, value):
    lstKEYS = list(a_dictionary.keys())

    for value_dictionary in lstKEYS:
        if value == a_dictionary.get(value_dictionary):
            del a_dictionary[value_dictionary]

    return (a_dictionary)
