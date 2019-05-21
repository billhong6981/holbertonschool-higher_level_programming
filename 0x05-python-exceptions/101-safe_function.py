#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct(*args)
        return (fct(*args))
    except ZeroDivisionError as err:
        sys.stderr.write('Exception: ' + str(err) + '\n')
        return (None)
    except IndexError as err:
        sys.stderr.write('Exception: ' + str(err) + '\n')
        return (None)
