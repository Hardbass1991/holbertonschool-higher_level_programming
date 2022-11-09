#!/usr/bin/python3
"""script that lists objects that contain the letter 'a'"""
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

    a = "%a%"
    rs = session.query(State).filter(State.name.like(a)).order_by(State.id)
    for r in rs:
        print(f"{r.id}: {r.name}")
