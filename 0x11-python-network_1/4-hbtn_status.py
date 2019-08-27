#!/usr/bin/python3
"""my http request module"""
import requests


if __name__ == '__main__':
    """my request http://url function"""
    url = 'https://intranet.hbtn.io/status'
    req = requests.get(url)
    print('Body response:')
    print('\t- type:', type(req.text))
    print('\t- content:', req.text)
