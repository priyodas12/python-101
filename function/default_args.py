
# some internal function

num_list=list(range(1,10))

for num in num_list:
    print(num)

print(type(num_list))

print(num_list.index(1,0,4))


def calculate_volume(length=1,breadth=1,height=1):
    return length*breadth*height


print(calculate_volume(2,3))
print(calculate_volume(breadth=5,length=3))

def calculate_sum(n1,n2,n3=2):
    return n1+n2+n3

#def calculate_sum(n1,n2=3,n3): #error
#    return n1+n2+n3

print(calculate_sum(2,5))

# Default arguments in Python are evaluated only once, at the time the function is defined, not each time the function is called.
# So if the default argument is mutable (like a list), changes to it persist across calls unless a new object is passed in.
def default_args_created_once(l=[1,2,3]):
    l.append(len(l))
    print(l)

default_args_created_once() #[1, 2, 3, 3]
default_args_created_once() #[1, 2, 3, 3, 4]

default_args_created_once([1,2])
default_args_created_once([1,2])
default_args_created_once()

# Takeaway: Avoid using mutable default arguments unless you're doing it intentionally.