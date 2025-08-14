test_list = [1, True, [2, 4, 5], "string", 8.493993, 5 + 9j]
print("---------------iterate with enumerate----------------")
# print list with index
for index, item in enumerate(test_list):
    print(f"{index} -- {item}")

print("---------------iterate with range----------------")
# another way
for i in range(len(test_list)):
    print(f"{i} -- {test_list[i]}")

print("----------------accessing elements---------------")
# accessing list
print(test_list[-1])  # last element
print(test_list[0])  # first element

print("---------------slicing----------------")
print(test_list[1:3])  # start_index(inclusive), end_index(exclusive)

print("---------------altering existing list----------------")
test_list[1] = "test_string"  # update with index
print(test_list)

test_list.append("next item added")
print(test_list)

test_list.insert(2, "adding at index 2")  # it will increase list length
print(test_list)

# gotcha
test_list.append([2, 4])  # add exact list
print(test_list)
test_list.extend([7, 8, 9])  # add each element individually
print(test_list)

# removing
test_list.remove([2, 4])  # remove  1st matching element
print(test_list)
test_list.pop(2)  # remove index 2
print(test_list)
test_list.pop()  # removes at last
print(test_list)

print("---------------search elements----------------")
test_list.extend([17, 18, 7])
print(test_list)
print(test_list.index(7))  # prints 1st searched index
print(test_list.count(7))  # count of occurrence

print("---------------sorting----------------")
lst = [34, 5, 7, 1, 9, 34, 22]
print(sorted(lst))  # sorted copy
print(lst)
lst.sort()  # now sorted
print(lst)

print("---------------copy in list----------------")
a = [1, 2, 3]
b = a
print(a)
print(b)

b.append(4)
print(b)
print(a)

c = [2, 3, 4]
d = c.copy()  # shallow copy

c.append(5)
print(c)
print(d)

print("---------------comprehension----------------")

mul = [x**2 for x in range(10)]
print(mul)

evens = [x % 2 == 0 for x in range(10)]
print(evens)

nums = [x for x in range(10)]
print(nums)

nums = list(range(10))
print(nums)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


primes = [x for x in range(100) if is_prime(x)]
print(primes)
