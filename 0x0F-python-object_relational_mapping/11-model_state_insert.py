#!/usr/bin/python3
"""add state"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def addstate(username, password, dbname):
    """function to add state"""
    db_url = f"mysql://{username}:{password}@localhost:3306/{dbname}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        louisiana = State(name="Louisiana")
        session.add(louisiana)
        session.commit()
        print(louisiana.id)

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
    addstate(username, password, dbname)
