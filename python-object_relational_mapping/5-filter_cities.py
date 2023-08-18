#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


def list_cities_based_on_state(user, passwd, db, state_name):
    '''List all cities ordered by id in
    ascending order'''
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db,
        port=3306)
    cursor = db.cursor()
    cursor.execute('''SELECT cities.name, states.name FROM cities\
    INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC;''')
    results = []
    for result in cursor.fetchall():
        if result[1] == state_name:
            results.append(result[0])
    print(', '.join(results))


if __name__ == '__main__':
    list_cities_based_on_state(argv[1], argv[2], argv[3], argv[4])
