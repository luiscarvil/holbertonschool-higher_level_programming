#!/usr/bin/python3
"""Start link class to table in database
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy import desc
import sys
from model_state import Base, State
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Lousiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
