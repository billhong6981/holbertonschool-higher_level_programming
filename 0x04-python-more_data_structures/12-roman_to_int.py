#!/usr/bin/python3
def roman_to_int(roman_string):
    def replace_str(str1, str_find, str_replace):
        idx = str1.find(str_find)
        if idx == 0:
            str1 = str_replace + str1[idx+2:]
        elif idx > 0:
            str1 = str1[:idx] + str_replace + str1[idx+2:]
        else:
            return
        return (str1)

    # return 0 when string is None or not in roman number
    sum1 = 0
    if type(roman_string) is not str or roman_string is None:
            return (sum1)
    # set up a roman number dictionary
    dict_roman = dict(M=1000, Z=900, D=500, T=400, C=100, G=90, L=50, Q=
                      40, X=10, P=9, V=5, R=4, I=1)
    list_a = ["CM", "CD", "XC", "IL", "IX", "IV"]
    list_b = ['Z', 'T', 'G', 'Q', 'P', 'R']
    for k, v in zip(list_a, list_b):
        if k in roman_string:
            roman_string = replace_str(roman_string, k, v)
    for i in range(len(roman_string)):
        sum1 += dict_roman[roman_string[i]]
    return (sum1)
