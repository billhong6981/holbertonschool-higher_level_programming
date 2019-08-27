#!/usr/bin/python3
"""my http request module"""
import urllib.request
from sys import argv


def reqst():
    """my request http://url function"""
    url = argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.info()
    print(header.get('X-Request-Id'))

if __name__ == '__main__':
    reqst()
