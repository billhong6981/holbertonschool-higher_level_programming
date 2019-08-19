#!/usr/bin/python3
"""This script that lists content of states"""
import MySQLdb
from sys import argv


def list_states():
    """my function that lists all states"""
    kwargs = {
        "host": "localhost",
        "user": argv[1],
        "passwd": argv[2]
        "db": argv[3]
        }
    conn = MySQLdb.connect(**kwargs)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == '__main__':
    list_states()
