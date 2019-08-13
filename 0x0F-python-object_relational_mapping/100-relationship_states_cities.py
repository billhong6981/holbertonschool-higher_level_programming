#!/usr/bin/python3
"""my module that lists all states"""
from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from relationship_city import City, Base
from relationship_state import State


def list_state():
    """list my states"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    st = State(name='California')
    ct = City(name='San Francisco')
    st.cities.append(ct)
    session.add_all([ct, st])
    session.commit()
    session.close()

if __name__ == "__main__":
    list_state()
