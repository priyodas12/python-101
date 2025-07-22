class Parent:
    def show(self):
        print("\nshow:: parent")


class Child1(Parent):
    def show(self):
        print("show:: child1")


class Child2(Parent):
    pass


class Child3(Parent):
    def show(self):
        super().show()
        print("show:: child2")


c1 = Child1()
c1.show()

c2 = Child2()
c2.show()

c3 = Child3()
c3.show()

# not allowed
# c2.super().show() # AttributeError: 'Child2' object has no attribute 'super'
