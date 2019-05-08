#!/usr/bin/python3
"""
a function prints all integers in the list

  my_list: a integers list

"""


def print_list_integer(my_list=[]):
    if len(my_list) == 0:
        return
    for i in range(len(my_list)):
        print('{:d}'.format(my_list[i]))
