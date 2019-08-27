#!/usr/bin/python3
"""a module requests http response"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user, auth=(argv[1], argv[2])"
    req = requests.get('https://api.github.com/user',
                       auth=(argv[1], argv[2]))
    if req.status_code == 200:
        dic = req.json()
        print(dic["id"])
    else:
        print("None")
