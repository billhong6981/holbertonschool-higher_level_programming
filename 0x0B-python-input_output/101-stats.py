#!/usr/bin/python3
"""my module"""
import sys


def print_fn(dic, size):
    """print function"""

    print("File size: {:d}".format(size))
    key = sorted(dic.keys())
    for k in key:
        if dic[k] != 0:
            print("{}: {}".format(k, dic[k]))


def main():
    """my main function"""

    size = 0
    dic = {"200": 0, "301": 0, "400": 0, "401": 0,
           "403": 0, "404": 0, "405": 0, "500": 0}
    n = 0
    try:
        for line in sys.stdin:
            n += 1
            l_s = line.split()
            try:
                size += int(l_s[-1])
            except:
                pass
            try:
                status = l_s[-2]
                if status in dic:
                    dic[status] += 1
            except:
                pass
            if n % 10 == 0:
                print_fn(dic, size)
        print_fn(dic, size)
    except KeyboardInterrupt:
        print_fn(dic, size)
        raise

if __name__ == "__main__":
    main()
