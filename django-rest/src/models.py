from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth = Column(DateTime)
    created_time = Column(DateTime, default=datetime.utcnow())

    def __repr__(self):
        return (
            f"User model, id = {self.id}",
            f"name: {self.first_name} {self.last_name}"
        )
