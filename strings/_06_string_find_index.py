s1="find a index"
# find(substr,startIndex,endIndex)
# Use find() when you're not sure if the substring exists.
# If not found, returns -1.
# Searches from left to right (start to end).
result=s1.find('a',0,len(s1))
print(f'find a index: {result}')

# Searches from right to left (end to start).
result=s1.rfind('n',0,len(s1))
print(f'find a reverse index: {result}')

# Both return -1 if the substring is not found, so they are safe to use without needing a try-except.

# index(subStr)
# index() when you're sure it exists and want a clean error if it doesn’t.
# Raises a ValueError if the substring is not found.
result=s1.index('i',0,len(s1))
print(f'index of i: {result}')

result=s1.rindex('x',0,len(s1))
print(f'rindex of x: {result}')

#result=s1.index('z',0,len(s1)) #ValueError: substring not found
#print(result)


result=s1.count('i',0,len(s1))
print(f'count of i: {result}')