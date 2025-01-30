class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == "__main__":
    rectangle = Rectangle(4, 5)
    print("Rectangle area:", rectangle.area()) 
