list_of_numbers=[11,21,31,41]

# traverse list at a time
for x in list_of_numbers:
    print(x)

iterator=iter(list_of_numbers)
print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#StopIteration Error here
#print(next(iterator))

numbers=range(3,10)

it1=iter(numbers)
print(next(it1))
