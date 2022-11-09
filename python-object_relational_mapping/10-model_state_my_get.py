#!/usr/bin/python3
"""script that lists objects that match argv[4]"""
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

    r = session.query(State).filter(State.name.like(a[4]))

    try:
        print(r[0].id)
    except IndexError:
        print("Not found")
