class BMW:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "250km/h"
    def display(self):
        return "This is a BMW car"
class Ferrari:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "340km/h"
    def display(self):
        return "This is a Ferrari car"
def car_info(car):
    print(car.display())
    print("Fuel Type:", car.fuel_type())
    print("Max Speed:", car.max_speed())
    print("-" * 30)
bmw = BMW()
ferrari = Ferrari()
car_info(bmw)
car_info(ferrari)