"""
Immutable sequence type in Python.
Stores ordered items.
Can hold mixed types (numbers, strings, objects… anything).
Created with parentheses () or without, if separated by commas.
"""

tuple1 = (1, 2, 3)
tuple2 = "abc", "bca", "cab"
empty = ()
single = (12,)

# indexing
print(tuple1[1])
print(tuple2)
print(type(tuple2))  # <class 'tuple'>

# slicing
print(tuple1[1:])
print(tuple2[:2])
print(tuple2[0:2])

# tuple unpacking
(
    a,
    b,
    c,
) = tuple2
print(
    a,
    b,
    c,
)

tuple3 = (
    1,
    2,
    3,
    4,
    5,
    6,
)

a, *mid, c = tuple3
print(a, mid, c)


def stat(a, b):
    return a + b, a * b, a / b, a % b  # returns tuple


print(stat(1232, 22))

tuple4 = ({a: 12, b: 22}, {a: 12, b: 22}, 12, "test")
# Immutable does not mean contents are all immutable.
tuple4[0][a] = 23

print(tuple4)

# iterating in tuple

for item in tuple4:
    print(item)

for index, item in enumerate(tuple3):
    print(index, item)

# concatenation
tuple5 = tuple3 + tuple4

print(tuple5)


# membership operation
t = (2, 6, 3, 9)
print(5 in t)
