#!/usr/bin/pyton3
def raise_exception_msg(message=""):
    try:
        raise NameError
    except:
        raise NameError(message)
