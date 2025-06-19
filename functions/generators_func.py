r=range(4)
print(r) #range(0, 4)

def custom_range(stop):
    i=0
    while i<stop:
        yield i
        i=i+1

values=custom_range(5)

for x in values:
    print(x)