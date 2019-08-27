#!/usr/bin/python3
"""my http request module"""
import urllib.request
import urllib.parse
from sys import argv


def reqst():
    """my request http://url function"""
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            header = response.read()
            print(header.decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)

if __name__ == '__main__':
    reqst()
