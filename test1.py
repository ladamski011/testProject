import math

class Point:
    'Class to represent a p'
    def __init__(self, x, y):
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return math.sqrt(
                (self.x - other_point.x)**2 +
                (self.y - other_point.y)**2)

# p1 = Point(5)
# p2 = Point(3, 4)
# print(p1.calculate_distance(p2))