#!/usr/bin/python3
def roman_to_int(roman_string):
    def replace_str(str=None, str_find=None, str_replace=None):
        idx = str.find(str_find)
        if idx == 0:
            str = str_replace + str[idx+2:]
        elif idx > 0:
            str = str[:idx] + str_replace + str[idx+2:]
        else:
            return
        return (str)

    # return 0 when string is None or not in roman number
    sum = 0
    if type(roman_string) is not str or roman_string is None:
            return (sum)

    # set up a roman number dictionary
    dict_roman = dict(M=1000, Z=900, D=500, T=400, C=100, G=90, L=50, Q=
40, X=10, P=9, V=5, R=4, I=1)
    list_a = ["CM", "CD", "XC", "IL", "IX", "IV"]
    list_b = ['Z', 'T', 'G', 'Q', 'P', 'R']

    for k, v in zip(list_a, list_b):
        if k in roman_string:
            roman_string = replace_str(roman_string, k, v)

    for i in range(len(roman_string)):
        sum += (dict_roman[roman_string[i]])
    return (sum)
