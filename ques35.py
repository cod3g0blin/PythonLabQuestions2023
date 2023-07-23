class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        print(f'Make: {self.make}')
        print(f'Model: {self.model}')
        print(f'Manufactured: {self.year}')


class Car(Vehicle):
    def __init__(self, make, model, year, horsePwr):
        super().__init__(make, model, year)
        self.horsePwr = horsePwr

    def startEngine(self):
        print('The engine has Started.')


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def wheelie(self):
        print('The motorcycle is doing a wheelie')


vehicle = Vehicle('Generic', 'Vehicle', 2023)
vehicle.get_info()

car = Car("Hyundai", "Verna", 2020, 400)
car.get_info()
car.startEngine()

bike = Motorcycle("Hero", "Splendor", 2015, 80)
bike.get_info()
bike.wheelie()
