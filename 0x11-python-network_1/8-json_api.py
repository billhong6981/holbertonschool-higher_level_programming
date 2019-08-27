#!/usr/bin/python3
"""a module requests http response"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 1:
        data = {"q": ""}
    else:
        data = {"q": argv[1]}
    try:
        req = requests.post(url, data)
        dic = req.json()
        if dic:
            print("[{}] {}".format(dic['id'], dic['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
