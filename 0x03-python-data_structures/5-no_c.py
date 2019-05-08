#!/usr/bin/python3
"""
a function that removes all characters c and C from a string.

    my_string: a given string

"""


def no_c(my_string):
    s = [my_string[i] for i in range(len(my_string))]
    for c in s:
        if c == 'c' or c == 'C':
            s.remove(c)
    s = "".join(map(str, s))
    return (s)
