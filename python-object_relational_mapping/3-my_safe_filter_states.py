#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
free form SQL injection
"""
from sys import argv
import MySQLdb


def list_states_matching_injection_safe(user, passwd, db, state_name):
    '''List all states ordered by id in
    ascending order that match "state_name"
    (SQL Injection safe)'''
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db,
        port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
    for result in cursor.fetchall():
        if result[1].startswith(state_name):
            print(result)


if __name__ == '__main__':
    list_states_matching_injection_safe(argv[1], argv[2], argv[3], argv[4])
