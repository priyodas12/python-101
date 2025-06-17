from datetime import datetime

def calculate_volume(length,breadth,height):
    print("length: {}, breadth: {}, height: {}".format(length,breadth,height))
    print("volume: {}, time: {}\n".format(length*breadth*height,datetime.now()))

# positional arguments
calculate_volume(1,2,3)

# keyword arguments
calculate_volume(breadth=1,length=2,height=3)
calculate_volume(10,breadth=2,height=3)

# SyntaxError: positional argument follows keyword argument
# calculate_volume(10,breadth=2,23);

calculate_volume(10,2,height=3)

# SyntaxError: positional argument follows keyword argument
# calculate_volume(length=12,202,height=3)

def print_seq(a,b,/,c,d,*,e,f):
    print(f"positional args: {a},{b}")
    print(f"positional or keywords args: {c},{d}")
    print(f"keyword args: {e},{f}")

print_seq(1,2,3,d=3,e=99,f=100)

