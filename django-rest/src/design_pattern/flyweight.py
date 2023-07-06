class ComplexCars:
    def __init__(self):
        pass

    def cars(self, car_name: str) -> str:
        return f"complex car: {car_name}"


class CarFamilies:
    car_family = {}

    def __new__(cls, name, car_family_id):
        try:
            _id = cls.car_family[car_family_id]
        except KeyError:
            _id = object.__new__(cls)
            cls.car_family[car_family_id] = _id
        return _id

    def set_car_info(self, car_info):
        cg = ComplexCars()
        self.car_info = cg.cars(car_info)

    def get_car_info(self):
        return self.car_info


if __name__ == '__main__':
    car_data = (('a', 1, 'Audi1'), ('a', 2, 'Ferrari'), ('b', 1, 'Audi2'))
    car_family_objects = []
    for i in car_data:
        obj = CarFamilies(i[0], i[1])
        obj.set_car_info(i[2])
        car_family_objects.append(obj)

    """similar id's says that they are same objects """

    for i in car_family_objects:
        print("id = " + str(id(i)))
        print(i.get_car_info())