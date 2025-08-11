# string is immutable, once created cannot be modified.
# modification will create new string

s1="hello"
s2=str(123)
print(f"example of strings: {s1}, {s2}")

name="priyobrato"
mail_broker="gmail.com"

print(f"my email: {name}@{mail_broker}")

# access string

s3='hello world!'
print(s3[0])
print(s3[-1]) # last index
print(s3[0:8:2])  # traverse with skip

# get string length
print(len(s3))

# function,variable or logic description
multi_line_str="""
hey
I 
am
multiline 
string...
"""

# incorporated single quote
s4="mark's marks"

print(s4)

print(s4[2])
# TypeError: 'str' object does not support item assignment
# s4[3]="test"
