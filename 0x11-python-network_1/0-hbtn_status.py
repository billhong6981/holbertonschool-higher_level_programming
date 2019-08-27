#!/usr/bin/python3
"""my http request module"""
import urllib.request


def reqst():
    """my request http://url function"""
    url = 'https://intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.read()
    print('Body response:')
    print('\t- type:', type(header))
    print('\t- content:', header)
    print('\t- utf8 content:', header.decode('UTF-8'))

if __name__ == '__main__':
    reqst()
