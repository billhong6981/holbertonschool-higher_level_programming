#!/usr/bin/python3
"""
    a function that retrieves an element from a list

    my_list: a integers list
    idx: a index

"""


def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return
    return (my_list[idx])
