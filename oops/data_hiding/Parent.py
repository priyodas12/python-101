class Parent:
    def __init__(self,d1,d2,d3):
        self.d1=d1
        self._d2=d2
        self.__d3 = d3

    def show(self):
        print(f"public_data:: {self.d1},"
              f"\nprotected_data:: {self._d2}"
              f"\nprivate_data:: {self.__d3}\n")


p=Parent("test data","private_data: can not be accessed","protected_data")
p.data="public data set"
p.__private_data=20 # will not be modified
p.show()
# ways to modify
p._Parent__private_data=30 # name mangling
p.show()

class Child(Parent):
    def __init__(self,d1,_d2,__d3):
        super().__init__(d1,_d2,__d3)

    def display(self):
        print(f"public: {self.d1}")
        print(f"protected: {self._d2}")
        print(f"private: {self.__d3}") # this will not be displayed:  AttributeError: 'Child' object has no attribute '_Child__d3'

c=Child(12,13,14)
c.show()
c.display()
