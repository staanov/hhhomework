class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, car_brand, car_model):
        self.car_brand = car_brand
        self.car_model = car_model

    def __repr__(self):
        return "{} - {}".format(self.car_brand, self.car_model)

class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars):
        self.cars = cars

    def __getitem__(self, position):
        return self.cars[position]

    def add(self, car):
        self.cars.append(car)

    def delete(self, index):
        self.cars.pop(index)
