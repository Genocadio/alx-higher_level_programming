#!/usr/bin/python3
"""list all states with letter a"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_Astates(username, password, dbname):
    """list all states with letter a"""
    db_url = f"mysql://{username}:{password}@localhost:3306/{dbname}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like("%a%"))\
        .order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    list_Astates(username, password, dbname)
