#!/usr/bin/python3
"""script that lists all State and City objects"""
if __name__ == '__main__':
    from sqlalchemy import (create_engine)
    from model_state import Base, State
    from model_city import City
    import sys

    a = sys.argv
    acc = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(acc.format(a[1], a[2], a[3]), pool_pre_ping=True)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()

    cs = session.query(City, State).\
        join(State, City.state_id == State.id).\
        order_by(City.id)
    for c in cs:
        print(f"{c[1].name}: ({c[0].id}) {c[0].name}")
