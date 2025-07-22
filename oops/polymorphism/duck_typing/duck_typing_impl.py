# If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck"
# Different types can be used interchangeably if they provide the required functionality
# Classes don’t have to be related by inheritance to be used interchangeably, as long as they share the needed interface
class Duck:
    def quack(self):
        print("Actual:: Quack!")


class Person:
    def quack(self):
        print("Mimic:: I'm pretending to be a duck!")


def make_it_quack(obj):
    obj.quack()


make_it_quack(Duck())  # Output: Quack!
make_it_quack(Person())  # Output: I'm pretending to be a duck!
