#!/usr/bin/python3
"""Say my name
Args:
    first_name: string
    last_name: string
"""


def say_my_name(first_name, last_name=""):
    """function prints my first name and last name
    Return: None
    """

    if first_name == "" or type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is", first_name, last_name)
