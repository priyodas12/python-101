"""
Syntax Error:

Logical Error:

Runtime Error

"""

a=input("enter value of a: ")
b=input("enter value of b: ")
#SyntaxError: unterminated string literal (detected at line 11): typing mistake
#b=input("enter value of b)

if int(a)>int(b):
    print("< a greater than b >")
else:
    #print("< b is greater than a >")
    print("< a greater than b >") # Logical error : use debugger

print(int(a)//int(b)) #ZeroDivisionError: division by zero -- Runtime Error