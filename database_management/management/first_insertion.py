from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import UserModel


def main():
    users = [
        UserModel(first_name="Ruicheng", last_name="Geng", birth=datetime(1997, 1, 1)),
        UserModel(first_name="Cool", last_name="Boy", birth=datetime(1997, 1, 2)),
    ]
    session_maker = sessionmaker(
        bind=create_engine(
            "postgresql+psycopg2://ruicheng:Grc201503030220@localhost:5005/ruicheng"
        )
    )
    with session_maker() as session:
        for user in users:
            session.add(user)
        session.commit()

    with session_maker() as session:
        user_records = session.query(UserModel).all()
        for user in user_records:
            print(user)


if __name__ == "__main__":
    main()
