from datetime import datetime
from typing import Callable, Iterable

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, UserModel


class User:
    """container of database instance of user"""
    def __init__(self, user_model: UserModel):
        self.id = user_model.id
        self.first_name = user_model.first_name
        self.last_name = user_model.last_name
        self.birth = user_model.birth


def do_with_session(func):
    session_maker = sessionmaker(
        bind=create_engine("postgresql+psycopg2://ruicheng:ruicheng@localhost:5432/ruicheng"))
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
        bind=create_engine("postgresql+psycopg2://ruicheng:ruicheng@localhost:5432/ruicheng"))
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
    for user in query_session(UserModel):
        print(user.id, user.first_name, user.last_name)


def delete_demo():
    items = []
    for user in query_session(UserModel):
        items.append(user)
    # items = [
    #     UserModel(first_name="Ruicheng", last_name="Geng", birth=datetime(1997, 1, 1)),
    #     UserModel(first_name="Cool", last_name="Boy", birth=datetime(1997, 1, 2))
    # ]

    def _delete_wrapper(session: Session):
        for item in items:
            session.delete(item)
            print(f"Deleted {item}")

    do_with_session(_delete_wrapper)


def update_demo():
    items = []
    for user in query_session(UserModel):
        items.append(User(user))

    def _update_wrapper(session: Session):
        for item in items:
            users = session.query(UserModel).filter_by(id=item.id).first()
            users.first_name = "rc"
            session.add(users)

    do_with_session(_update_wrapper)


if __name__ == '__main__':
    add_demo()
    print("First commit result...")
    read_table_demo()
    print("Doing update...")
    update_demo()
    print("Second commit result...")
    read_table_demo()
    print("Deleting table...")
    delete_demo()

