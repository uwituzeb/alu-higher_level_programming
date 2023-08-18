#!/usr/bin/python3
"""
prints the State object
with the name passed as argument from the database hbtn_0e_6_usa
"""


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
    results = []
    for instance in session.query(State).order_by(State.id):
        if argv[4] == instance.name:
            results.append(instance.id)
    if results == []:
        print('Not found')
    else:
        for r in results:
            print(r)
