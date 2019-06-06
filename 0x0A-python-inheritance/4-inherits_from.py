#!/usr/bin/python3
"""my module"""


def inherits_from(obj, a_class):
    """my function"""

    if type(obj) is a_class:
        return False
    elif issubclass(type(obj), a_class):
        return True
    return False
