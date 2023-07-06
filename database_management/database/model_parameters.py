from sqlalchemy import Column, Integer, Float,  String, DateTime, ForeignKey

from .base import Base
from .models import UserModel


class ModelSetting(Base):
    __tablename__ = "model_setting"

    model_version_id = Column(String(length=2048), ForeignKey(UserModel.model_version_id), unique=True, primary_key=True)

    display_name = Column(String(length=2048), nullable=False)
    decay_constant = Column(Float, nullable=True, default=0.015, server_default="0.015")
    factor_selection_method = Column(String(length=2048), nullable=False, default="method1", server_default="method1")
