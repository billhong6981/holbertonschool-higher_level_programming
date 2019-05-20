#!/usr/bin/python3
def safe_print_division(a, b):
    res = None
    try:
        res = a / b
    except ZeroDivisionError:
        pass
    finally:
        if res is not None:
            print("Inside result: {:3.1f}".format(res))
        else:
            print("Inside result: {}".format(res))
        return (res)
