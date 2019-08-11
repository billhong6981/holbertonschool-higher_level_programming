#!/usr/bin/python3
"""This script that lists content of states"""
import MySQLdb
from sys import argv


def list_states():
    """my function that lists all states"""
    kwargs = {
        "host": "localhost",
        "user": argv[1],
        "passwd": argv[2],
        "db": argv[3]
        }
    db = MySQLdb.connect(**kwargs)
    db.query("SELECT * FROM states ORDER BY id")
    r = db.store_result()
    z = r.fetch_row(maxrows=0)
    for i in z:
        print(i)

if __name__ == '__main__':
    list_states()
