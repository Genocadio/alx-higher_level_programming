#!/usr/bin/python3
"""prints city"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def get_city(username, password, dbname):
    """function to print city"""
    db_url = f"mysql://{username}:{password}@localhost:3306/{dbname}"

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        cities = session.query(City, State).filter(City.state_id == State.id)\
            .order_by(City.id).all()
        for city, state in cities:
            print(f"{state.name}: ({city.id}) {city.name}")

    except Exception as e:
        print("Error:", e)
    finally:
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    get_city(username, password, dbname)
