import math
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
c=circle(7)
print("Area of circle is: ",c.area())
print("Perimeter of circle is: ",c.perimeter())