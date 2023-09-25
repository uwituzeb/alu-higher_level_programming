#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


def list_states(username, password, db_name):
    """
    listing all states
    """
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            password=password,
            db=db_name,
            port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
    for result in cursor.fetchall():
        print(result)


if __name__ == '__main__':
    list_states(argv[1], argv[2], argv[3])
