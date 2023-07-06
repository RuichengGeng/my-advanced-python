from .singleton import FancyLogger
from .singleton_try import singleton_test


def singleton_test2():
    singleton_test()
    local_logger = FancyLogger.get_instance()
    local_logger.log("test message 2")
    local_logger.print_log()


if __name__ == "__main__":
    singleton_test2() # it shows singleton works as expected