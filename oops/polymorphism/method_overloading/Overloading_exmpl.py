print(len("str"))
print(len([123,233,899,33]))
print(len((123,21,899,33)))

# function with same name -type of parameter is different and number of parameter is different

# type of different parameter is obvious in python by default

# let's have a glance of - function with different number of parameter

def sum_of_digit(a, b):
    return a+b

def sum_of_digit(a, b,c):
    return a+b+c
# TypeError: sum_of_digit() missing 1 required positional argument: 'c'
# by default it will be hidden: use Variable-Length Arguments: Use *args and **kwargs to accept arbitrary numbers of positional and keyword arguments
# sum_of_digit(12,34)
print(sum_of_digit(23,34,324))

