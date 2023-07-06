import functools
from .calculation_servicer import CalculationServicer, CalculationServicerImplementation
import logging

_logger = logging.getLogger(__name__)


class ServiceFactory:
    __instance = None

    @staticmethod
    def get_instance():
        if ServiceFactory.__instance is None:
            _logger.warning("Error no instance found, create one!")
            return ServiceFactory()
        return ServiceFactory.__instance

    def __init__(self):
        if ServiceFactory.__instance is not None:
            raise Exception("already has an instance, can't have more than 1...")
        ServiceFactory.__instance = self

    @functools.cached_property
    def calculation_servicer(self) -> CalculationServicer:
        return CalculationServicerImplementation()
