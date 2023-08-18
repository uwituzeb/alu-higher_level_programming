#!/usr/bin/python3
"""
 script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


def list_states_starting_with_N(user, passwd, db):
    '''List all states ordered by id in
    ascending order that start with "N"'''
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db,
        port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
    for result in cursor.fetchall():
        if result[1].startswith('N'):
            print(result)


if __name__ == '__main__':
    list_states_starting_with_N(argv[1], argv[2], argv[3])
    