class Outer:
    def __init__(self,d):
        self.in_obj=self.Inner(d)

    def show(self):
        print("Outer: calling inner class")
        self.in_obj.display()


    class Inner:
        def __init__(self,data):
            self.data=data

        def display(self):
            print(f"Inner : property - {self.data}")

o=Outer(1213)
o.show()

