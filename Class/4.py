import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


p1 = Point(1, 2)
p2 = Point(4, 6)
print("Distance:", p1.dist(p2))