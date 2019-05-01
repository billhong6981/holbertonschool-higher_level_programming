#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        val = ord(str[i])
        if val >= 97 and val <= 123:
            val = val - 32
        if i != len(str) - 1:
            print('{:c}'.format(val), end="")
    else:
        print('{:c}'.format(val))
