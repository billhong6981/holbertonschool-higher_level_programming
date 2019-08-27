#!/usr/bin/python3
"""a module requests http response"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
        .format(argv[2], argv[1])
    req = requests.get(url)
    if req.status_code == 200:
        dic = req.json()
        try:
            for i in range(10):
                a = dic[i]
                print("{}: {}".format(a["sha"], a["commit"]["author"]["name"]))
        except:
            pass
