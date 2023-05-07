class Vehicle:
    def __init__(self, price, color):
        self.color = color
        self.price = price
        self.gas = 0

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


class Truck(Vehicle):
    def __init__(self, price, color, tires):
        Vehicle.__init__(self, price, color)
        self.tire = tires

    def beep(self):
        print("Honk")


class Car(Vehicle):
    def __init__(self, price, color, tires):
        Vehicle.__init__(self, price, color)
        self.tire = tires

    def beep(self):
        print("Beep")


car = Car(10000, "Red", 60)
truck = Truck(50000, "Black",16)

car.beep()
car.fillUpTank()
print(car.gasLeft())

truck.beep()
truck.fillUpTank()
print(truck.gasLeft())
