s1="hello india"
# returns a new string left-justified in a field of specified width.
result=s1.ljust(len(s1)+10,'.')
print(f'left adjusted of s1: {result}')

# returns a new string right-justified in a field of specified width.
result=s1.rjust(len(s1)+10,'*')
print(f'right adjusted of s1: {result}')

# returns a new string center-justified in a field of specified width.
result=s1.center(len(s1)+10,'*')
print(f'center adjusted of s1: {result}')

# strip: by default it removes white space
result=result.strip("*")
print(f'after striping of s1: {result}')