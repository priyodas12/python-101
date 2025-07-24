dict1=dict({1:"one",2:"two",3:"three"})

print(type(dict1.keys()))
print(type(dict1.values()))

print(dict1.values())
# accessing the dictionary
print(dict1.items())
print(dict1[1]) # KeyError: 2 if key does not exist

# write or modify
dict1[100]="hundred"
print(dict1)

# traverse: only provide keys
for item in dict1:
    print(item)

# traverse: both key values
for item in dict1.items():
    print(item)