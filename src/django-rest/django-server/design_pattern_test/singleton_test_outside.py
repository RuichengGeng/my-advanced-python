import design_pattern

local_logger = design_pattern.FancyLogger.get_instance()


def outside_main():
    design_pattern.singleton_try_again.singleton_test2()
    local_logger.log("test message outside")
    local_logger.print_log()


if __name__ == "__main__":
    outside_main()

