#!/usr/bin/python3
"""delete state with a"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def del_Astate(username, password, dbname):
    """delete state with a"""
    db_url = f"mysql://{username}:{password}@localhost:3306/{dbname}"

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        states_to_delete = session.query(State).filter(State.name.like("%a%")).all()
        for state in states_to_delete:
            session.delete(state)
        session.commit()

    except Exception as e:
        print("Error:", e)
        session.rollback()
    finally:
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    del_Astate(username, password, dbname)
