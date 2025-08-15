"""
Unordered collection of unique elements.
Mutable (you can add/remove items).
Supports fast membership checks (in / not in) because it uses a hash table internally.
Elements must be hashable (immutable types like numbers, strings, tuples without mutable parts).
"""

s = {1, 2, 3, 4}
print(type(s))

s2 = set([1, 2, 2, 3])  # removes duplicate
print(s2)

s3 = set(list([3, 5, 9, 7, 2, 9]))
print(s3)


# adding element
s3.add(23)
print(s3)
# discard element
s3.discard(7)
print(s3)

# removes arbitrary element
s3.pop()
print(s3)

# clear all
s3.clear()
print(s3)

# math style operations

a = {2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))  # union

print(a & b)  # intersection

print(b - a)

print(a.symmetric_difference(b))  # un-common elements
