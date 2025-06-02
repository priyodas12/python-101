# replace old subString and new subString

s1="old string archive"

result=s1.replace("old","new");
print(f'replacement : {result}')

# join string
words = ["Hello", "world", "from", "Python"]
result=" _*_ ".join(words)
print(f'after joining iterable : {result}')

nums = [1, 2, 3]
result = "-".join(str(num) for num in nums)
print(f'after joining numbers : {result}')

# split string
result=s1.split(" ") # reruns list
print(f'after splitting numbers : {result}')
print(type(result)) #<class 'list'>

multi_lines="""
just
a
multiline
string
.
"""

result=multi_lines.splitlines()
print(f'after splitting multi line : {result}')