import math

class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi*(self.radius**2)*self.height

    def surface_area(self):
        return 2*(math.pi)*self.radius*self.height + (2*math.pi*self.radius**2)


cyl = Cylinder(2,3)
print(f"Volume is {cyl.volume()}")
print(f"Surface Area is {cyl.surface_area()}")
