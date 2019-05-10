#!/usr/python3
def search_replace(my_list, search, replace):
    n_list = my_list.copy()

    idx = n_list.index(search)
    n_list.remove(search)
    n_list.insert(idx, replace)

    return (n_list)
