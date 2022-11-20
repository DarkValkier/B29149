class CarNotEnoughFuel(Exception):
    def __init__(self, message='Не хватит топлива!'):
        Exception.__init__(self, message)


class Car:
    fuel = 20
    rate = 0.1
    traveled = 0

    def __init__(self, fuel=20, rate=0.1):
        self.fuel = fuel
        self.rate = rate

    def __str__(self):
        return f'fuel: {self.fuel}\n' \
               f'rate: {self.rate}\n' \
               f'traveled: {self.traveled}\n'

    def drive(self, distance):
        if self.fuel < distance * self.rate:
            raise CarNotEnoughFuel('Не хватит топлива!')
        else:
            self.traveled += distance
            self.fuel -= distance * self.rate


car1 = Car()
print(car1)
try:
    car1.drive(-3)
except CarNotEnoughFuel:
    print('Не хватит топлива для поездки. Ищем ближайшую заправку.')
print(car1)