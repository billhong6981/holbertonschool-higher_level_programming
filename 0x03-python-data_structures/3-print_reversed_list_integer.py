#!/usr/bin/python3
"""

    a function that prints all integers of a list, in reverse order.

        my_list: a list

"""


def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return
    for i in reversed(range(len(my_list))):
        print('{:d}'.format(my_list[i]))
