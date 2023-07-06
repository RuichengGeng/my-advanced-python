import copy


class Memento:
    def __init__(self, status, data):
        self.status = status
        self.data = data


class ModelUpdater:
    def __init__(self):
        self.status = 0
        self.data = []

    def update_model(self, model):
        self.status += 1
        self.data.append(model)

    def save_model(self):
        return Memento(self.status, copy.deepcopy(self.data))

    def rollback_model(self, memo):
        self.status = memo.status
        self.data = memo.data


class ModelUpdaterUtility:
    __instance = None

    @staticmethod
    def get_instance():
        if ModelUpdaterUtility.__instance is None:
            print("Error no instance found, create one!")
            return ModelUpdaterUtility()
        return ModelUpdaterUtility.__instance

    def __init__(self):
        if ModelUpdaterUtility.__instance is not None:
            raise Exception("already has an instance, can't have more than 1...")
        self._memo = {}
        ModelUpdaterUtility.__instance = self

    def save(self, updater: ModelUpdater):
        self._memo[type(updater)] = updater.save_model()

    def rollback(self, updater: ModelUpdater):
        updater.rollback_model(self._memo[type(updater)])

    def clear_memo(self):
        self._memo = {}


if __name__ == "__main__":
    model_utility = ModelUpdaterUtility.get_instance()
    model_updater = ModelUpdater()

    model_updater.update_model("update1")
    print('model1', model_updater.status)
    print('model1', model_updater.data)

    model_updater.update_model("update2")
    print('model2', model_updater.status)
    print('model2', model_updater.data)

    model_updater.update_model("update3")
    print('model3', model_updater.status)
    print('model3', model_updater.data)

    model_utility.save(model_updater)

    model_updater.update_model("update4")
    print('model4', model_updater.status)
    print('model4', model_updater.data)

    model_utility.rollback(model_updater)
    print('model4', model_updater.status)
    print('model4', model_updater.data)



