from .singleton import main, FancyLogger


def singleton_test():
    main()
    local_logger = FancyLogger.get_instance()
    local_logger.log("test message")
    local_logger.print_log()


if __name__ == "__main__":
    singleton_test()
