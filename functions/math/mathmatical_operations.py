from pygments.lexer import default

n=178293.239203

print(abs(-2738)) # always returns positive
print(abs(-25+8j)) # modules value

print(pow(10,2))
print(pow(10,-2))
print(pow(5,2,3)) # after power calculation result % 3(25%3=1)

print(round(n))
print(round(n,2)) # decimal precision

# special case

print(round(4.5),round(5.5)) # 4,6- Bankers rounding

print(divmod(23,7)) # result - (23/7,23%7)

num_list=[23.77,21.4552,9,89,0,88,-6]

print(min(num_list))
print(max(num_list))
print(min([],default="empty list"))

print(sum(num_list))

print(eval("34*67-23+83/4*526"))