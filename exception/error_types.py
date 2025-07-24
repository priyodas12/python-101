"""
Syntax Error:

Logical Error:

Runtime Error

"""

a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
#SyntaxError: unterminated string literal (detected at line 11): typing mistake
#b=input("enter value of b)

if a>b:
    print("< a greater than b >")
else:
    #print("< b is greater than a >")
    print("< a greater than b >") # Logical error : use debugger

print(a//b) #ZeroDivisionError: division by zero -- Runtime Error