#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""
if __name__ == '__main__':
    from sqlalchemy import (create_engine)
    from model_state import Base, State
    import sys

    a = sys.argv
    acc = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(acc.format(a[1], a[2], a[3]), pool_pre_ping=True)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id)
    i = 0
    for result in results:
        i += 1
        print(f"{i}: {result.name}")
