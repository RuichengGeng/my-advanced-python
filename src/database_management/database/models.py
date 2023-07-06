from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from .base import Base


class UserModel(Base):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True, autoincrement=True)
    model_version_id = Column(String(length=2048), nullable=False, unique=True, primary_key=True)
    created_time = Column(DateTime, default=datetime.utcnow)
