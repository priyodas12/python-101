class Rectangle:
    def __init__(self):
        self.length=10
        self.breadth=20

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

rectangle=Rectangle()

print(f"Area of Rectangle: {rectangle.area()}")

print(f"Perimeter of Rectangle: {rectangle.perimeter()}")