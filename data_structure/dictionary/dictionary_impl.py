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

dict2=dict({1:"one",2:2.0,3:4+7j,4:True,5:[4,5,6],6:(9,6,7),7:{100.992,923.3434,747.734}})

for item in dict2.values():
    print(type(item),"->",item)

# keys only immutable datatype: list,sets not allowed, only tuple allowed
# TypeError: unhashable type: 'list'
# dict3=dict({[1,3,4,5]:"one",21:"21",32:"32"})
dict3=dict({(1,2):"one,two",3+7j:"21",32.239:"32"})

for item in dict3.keys():
    print(type(item),"->",item)
