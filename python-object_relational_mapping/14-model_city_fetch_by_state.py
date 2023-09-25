#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""


from sys import argv

from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(City).order_by(City.id):
        state_data = session.query(State).filter_by(id=instance.state_id).one()
        state_name = state_data.name
        print(f"{state_name}: ({instance.id}) {instance.name}")
