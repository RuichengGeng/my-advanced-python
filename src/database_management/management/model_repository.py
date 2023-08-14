import abc

from .connection import BaseRepository


class IModelRepository(abc.ABC):
    def get_all_models(self):
        ...

    def get_model_setting(self, model_version_id: str):
        ...


class DatabaseModelRepository(IModelRepository):
    pass