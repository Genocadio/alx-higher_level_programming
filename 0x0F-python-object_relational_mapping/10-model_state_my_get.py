#!/usr/bin/python3
"""list state by name"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def find_state_by_name(username, password, dbname, s_name):
    """list state by name"""
    db_url = f"mysql://{username}:{password}@localhost:3306/{dbname}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).filter(State.name == s_name).first()
        if state:
            print(state.id)
        else:
            print("Not found")
    except Exception as e:
        print("Error:", e)
    finally:
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    s_name = sys.argv[4]
    find_state_by_name(username, password, dbname, s_name)
