#!/usr/bin/python3
"""my http request module"""
import urllib.request
import urllib.parse
from sys import argv


def reqst():
    """my request http://url function"""
    url = argv[1]
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        header = response.read()
    print(header.decode('UTF-8'))

if __name__ == '__main__':
    reqst()
