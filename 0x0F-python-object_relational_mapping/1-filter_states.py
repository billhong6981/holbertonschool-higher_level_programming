#!/usr/bin/python3
"""This script that lists content of states"""
import MySQLdb
from sys import argv


def list_states():
    """my function that lists states start with N"""
    kwargs = {
        "host": "localhost",
        "user": argv[1],
        "passwd": argv[2],
        "db": argv[3]
        }
    db = MySQLdb.connect(**kwargs)
    db = db.cursor()
    db.execute("""SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id""")
    z = db.fetchall()
    for i in z:
        print(i)

if __name__ == '__main__':
    list_states()
