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
        sys.argv[1],
        sys.argv[2],
        sys.argv[3])
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_first = session.query(State).filter_by(name=sys.argv[4]).first()
    if state_first is not None:
        print("{}".format(state_first.id))
    else:
        print("Not found")
    session.close()
