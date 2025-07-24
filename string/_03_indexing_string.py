s5="Hello India!"

# skipping even characters
# str[start:stop:step] : similar like range function
# forward way
print(s5[0:len(s5):2])

# backword way
print(s5[-len(s5):-1:2])

print(s5[::2])

# string reverse
print(s5[-3::-1])