class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed=max_speed
        self.mileage=mileage
class bus(Vehicle):
    def __str__(self):
        return ("vehicle name {}, Speed {}, Mileage {}".format(self.name, self.max_speed, self.mileage))

School_bus = bus("school volvo", 180, 12)
print(School_bus)
