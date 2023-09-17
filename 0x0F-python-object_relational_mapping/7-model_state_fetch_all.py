#!/usr/bin/python3
"""lists all states from db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, dbname):
    """lists all states from db"""
    db_url = f"mysql://{username}:{password}@localhost:3306/{dbname}"

    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    list_states(username, password, dbname)
