import math

class Line:

    def __init__(self, coor1, coor2):
        self.coordinate1 = coor1
        self.coordinate2 = coor2

    def distance(self):
        return abs(math.sqrt(((self.coordinate2[0] - self.coordinate1[0])**2) + (self.coordinate2[1] - self.coordinate1[1])**2))

    def slope(self):
        return ((self.coordinate2[1] - self.coordinate1[1]) / (self.coordinate2[0] - self.coordinate1[0]))


li = Line((3,2), (8,10))
print(f"The distance is {li.distance()}")
print(f"The slope is {li.slope()}")
