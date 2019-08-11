#!/usr/bin/python3
"""my module that lists all cities"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_city import City


def list_city():
    """list my cities"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for city, state in session.query(City, State)\
                              .filter(State.id == City.state_id)\
                              .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()

if __name__ == "__main__":
    list_city()
