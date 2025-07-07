class Rectangle:
    def __init__(self,length,breadth):
        print("init method called")
        print(id(self),length,breadth)
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

r1=Rectangle(232,74)

print(f"Area of Rectangle: {r1.area()}")

print(f"Perimeter of Rectangle: {r1.perimeter()}")

print(id(r1))

# self : reference to the current object