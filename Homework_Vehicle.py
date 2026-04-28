class Vehicle:
    def __init__(self, name, total_fare, mileage):
        self.name = name
        self.total_fare = total_fare
        self.mileage = mileage
class Bus(Vehicle):
    pass
school_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", school_bus.name, 
      "Total Fare:", school_bus.total_fare, 
      "Mileage:", school_bus.mileage)