# variables and methods
#----------------------
#   instance
#   class
#   static
#-----------------------
class Rectangle:
    def __init__(self,length,breadth):
        # instance variable
        self.length=length
        self.breadth=breadth

    #  instance methods: self should be the first parameter
    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

r1=Rectangle(232,74)

print(f"Area of Rectangle: {r1.area()}")

print(f"Perimeter of Rectangle: {r1.perimeter()}")

print(id(r1))

class Test:
    def __init__(self):
        self.a=10

    # not recommended
    def func1(self):
        self.b=20

    def print_variables(self):
        print(f"printing instance variable of class Test")
        print(self.a,self.b,self.c)

t1=Test()
t1.func1()
# not the right way
t1.c=30
t1.print_variables()