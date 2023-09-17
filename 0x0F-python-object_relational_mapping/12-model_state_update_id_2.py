#!/usr/bin/python3
"""change name of state"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def changename(username, password, dbname):
    """change name of state"""
    db_url = f"mysql://{username}:{password}@localhost:3306/{dbname}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state_to_update = session.query(State).filter_by(id=2).first()
        if state_to_update:
            state_to_update.name = "New Mexico"
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
    changename(username, password, dbname)
