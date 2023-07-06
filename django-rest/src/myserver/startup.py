import logging

from .servicer_factory import ServiceFactory
_logger = logging.getLogger(__name__)


def startup_server():
    _logger.info("Preparing servicer provider...")
    ServiceFactory.get_instance()
