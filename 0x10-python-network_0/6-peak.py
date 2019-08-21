#!/usr/bin/python3
"""my module"""


def find_peak(list_of_integers):
    """my function"""
    if len(list_of_integers) == 0:
        return (None)
    if len(list_of_integers) == 1:
        return (list_of_integers[0])
    binary_list = []
    j = len(list_of_integers) - 1
    i = 0
    while (i < j):
        if list_of_integers[i] > list_of_integers[j]:
            temp = list_of_integers[i]
        else:
            temp = list_of_integers[j]
        binary_list.append(temp)
        i += 1
        j -= 1
        if (i == j):
            binary_list.append(list_of_integers[j])
            break
    return (find_peak(binary_list))
