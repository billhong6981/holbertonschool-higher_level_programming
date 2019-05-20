#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except IndexError:
            pass
    print()
    return (x if x < len(my_list) else len(my_list))
