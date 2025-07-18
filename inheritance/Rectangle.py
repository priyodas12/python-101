class Rectangle:
    def __init__(self, length, breadth):
        print("parent class constructor")
        self.length = length
        self.breadth = breadth

    def get_area(self):
        return self.breadth * self.length


class Cuboid(Rectangle):
    def __init__(self, length, breadth, height):
        print("child class constructor")
        super().__init__(length, breadth)
        self.height = height

    def get_volume(self):
        return self.height * self.length * self.breadth


cuboid = Cuboid(1034, 56, 82)
print(f"volume:  {cuboid.get_volume()}")
