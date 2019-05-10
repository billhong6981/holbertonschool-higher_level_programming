#!/usr/python3
"""
    a function replaces the element in the list
"""

def search_replace(my_list, search, replace):
    return ([replace if x is search else x for x in my_list])
