class FancyLogger:
    __instance = None

    @staticmethod
    def get_instance():
        if FancyLogger.__instance is None:
            print("Error no instance found, create one!")
            return FancyLogger()
        return FancyLogger.__instance

    def __init__(self):
        if FancyLogger.__instance is not None:
            raise Exception("already has an instance, can't have more than 1...")
        self._log = []
        FancyLogger.__instance = self

    def log(self, msg):
        self._log.append(msg)

    def print_log(self):
        for _msg in self._log:
            print(_msg)


class BorgSingleton:
    __shared_state = {}
    _count = 0

    def __init__(self):
        self.__dict__ = BorgSingleton.__shared_state
        self.state = "cool"
        self._count += 1

    def __str__(self):
        return self.state

    def report_count(self):
        print(self._count)


def main():
    logger1 = FancyLogger.get_instance()
    logger1.log("first message")
    logger1.print_log()

    logger2 = FancyLogger.get_instance()
    logger2.log("second message")
    logger2.print_log()


    # b = BorgSingleton()
    # b.state = "b"
    # print(b)
    # b.report_count()
    #
    # c = BorgSingleton()
    # c.state = "c"
    # print(c)
    # c.report_count()
    #
    # t = c.__dict__
    # print(t)


if __name__ == "__main__":
    main()
