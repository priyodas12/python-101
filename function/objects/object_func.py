s="priyo das"
print(type(s))
print(type(23))
print(type(23.3))
print(type((1,2,3)))
print(type([1,2,3]))
print(type({1,2,3}))
print(type({"test":23,"foo":True}))
print(type(None)) #NoneType

print(isinstance(s,str)) #True
print(isinstance(23,float)) #False
print(isinstance(23,(float,int,str))) #True

print(id(s)) #memeory address
l1={1,2,3}
l2={1,2,3}

print(id(l1),id(l2)) # 139345613512192 139345613510624

print(repr(s)) # actual representation