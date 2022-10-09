from datetime import datetime
from typing import Callable, Iterable

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, UserModel



def do_with_session(func):
    session_maker = sessionmaker(
        bind=create_engine("postgresql+psycopg2://ruicheng:Grc201503030220@localhost:5005/ruicheng"))
    with session_maker() as session:
        try:
            func(session)
        except:
            session.rollback()
            raise
        else:
            session.commit()


def query_session(table: Base):
    session_maker = sessionmaker(
        bind=create_engine("postgresql+psycopg2://ruicheng:Grc201503030220@localhost:5005/ruicheng"))
    with session_maker() as session:
        try:
            records = session.query(table).all()
            for record in records:
                yield record
        except:
            session.rollback()
            raise
        else:
            session.commit()


def add_demo():
    items = [
        UserModel(first_name="Ruicheng", last_name="Geng", birth=datetime(1997, 1, 1)),
        UserModel(first_name="Cool", last_name="Boy", birth=datetime(1997, 1, 2))
    ]
    def _add_wrapper(session: Session):
        for item in items:
            session.add(item)

    do_with_session(_add_wrapper)


def read_table_demo():
    with session_maker() as session:
        user_records = session.query(UserModel).all()
        for user in user_records:
            print(user)


def delete_wrapper(items: Iterable, session: Session):
    for item in items:
        session.delete(item)


if __name__ == '__main__':
    add_demo()
