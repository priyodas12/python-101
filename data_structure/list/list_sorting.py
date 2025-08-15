names = ["alice", "bob", "carol", "avian", "cesar"]
print(names)
sorted_names_by_length = sorted(names, key=lambda x: len(x))
print(sorted_names_by_length)

sorted_names_by_1st_character = sorted(names, key=lambda x: len(x[0]))
print(sorted_names_by_1st_character)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Implement __repr__ for debugging.
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    # Implement __str__ if you want a nice string for printing.
    def __str__(self):
        return f"Person: [name={self.name}, age={self.age}]"


person1 = Person("Alice", 81)
person2 = Person("Bob", 43)
person3 = Person("Carol", 22)
person4 = Person("Avian", 72)
person5 = Person("Avian", 92)

list1 = [person1, person2, person3, person4, person5]

print(person1)
print(str(person1))
print(repr(person1))

sorted_by_age = sorted(list1, key=lambda x: x.age)
print(sorted_by_age)

# multiple sorting
sorted_by_age_then_name = sorted(
    list1,
    key=lambda x: (
        x.name[2],
        x.age,
    ),
)
print(sorted_by_age_then_name)
