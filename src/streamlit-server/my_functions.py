import logging

_logger = logging.getLogger("my_logger")


def foo():
    _logger.info("calling foo function...")
    logging.warning("this is a warning message")
    return "foo"
