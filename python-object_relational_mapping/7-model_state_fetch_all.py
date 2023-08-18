#!/usr/bin/python3
"""
that lists all State objects from the database hbtn_0e_6_usa
"""


import MySQLdb
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(f"{instance.id}: {instance.name}")
