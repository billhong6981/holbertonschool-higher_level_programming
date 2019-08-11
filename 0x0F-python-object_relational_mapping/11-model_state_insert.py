#!/usr/bin/python3
"""my module that lists all states"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


def list_state():
    """list my states"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    st = State(name='Louisiana')
    session.add(st)
    st_add = session.query(State).filter_by(name='Louisiana').first()
    session.commit()
    print(st_add.id)
    session.close()

if __name__ == "__main__":
    list_state()
