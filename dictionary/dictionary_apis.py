d1={1:"one",2:"two",3:"three"}

# iterable pairs

d2=dict([(1,"one"),(2,"two"),(3,"three")])
for key in d2:
    print(key,d2[key])

# zip functions

l1=[1,2,3,4]
l2=["one","two","three","four","five"]

d3=zip(l1,l2)
for item in d3:
    print(item)

# enumerate function

d4=enumerate(l2,start=1)
for item in d4:
    print(item)

