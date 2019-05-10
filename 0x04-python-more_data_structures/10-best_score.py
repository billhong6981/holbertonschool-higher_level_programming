#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        value_list = list(a_dictionary.values())
        best_p = max(value_list)
        for k, v in a_dictionary.items():
            if v is best_p:
                return (k)
    return
