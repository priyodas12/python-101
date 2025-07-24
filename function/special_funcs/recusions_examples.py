def print_nums(start,limit):
    if start<limit:
        print(start)
        print_nums(start+1,limit)

print_nums(0,10)

def print_numbers(num):
    if num>0:
        print_numbers(num-1)
        print(num)
print("\n\n")
print_numbers(10)