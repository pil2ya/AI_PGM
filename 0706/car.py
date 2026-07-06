class Car:
    def __init__(self, make, color, model, price):
        self.make = make
        self.color = color
        self.model = model
        self.price = price
    def set_make(self, make):
        self.make = make
    def get_make(self):
        return self.make
    def __str__(self):
        return f"Car(make={self.make}, color={self.color}, model={self.model}, price={self.price})"

class ElectricCar(Car):
    def __init__(self, make, color, model, price, battery_capacity):
        super().__init__(make, color, model, price)
        self.battery_capacity = battery_capacity
    def set_battery_capacity(self, battery_capacity):
        self.battery_capacity = battery_capacity
    def get_battery_capacity(self):
        return self.battery_capacity
    def __str__(self):
        return f"ElectricCar(make={self.make}, color={self.color}, model={self.model}, price={self.price}, battery_capacity={self.battery_capacity})"

myCar = ElectricCar("Tesla", "Red", "Model S", 80000, 100)
print(myCar)  # ElectricCar(make=Tesla, color=Red, model=Model S, price=80000, battery_capacity=100)