#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
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
    result = session.query(State.name).first()
    if result is None:
        print('Nothing')
    else:
        print(f"1: {result[0]}")
