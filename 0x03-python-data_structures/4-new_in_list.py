#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_new = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return (my_list_new)
    my_list_new[idx] = element
    return (my_list_new)
