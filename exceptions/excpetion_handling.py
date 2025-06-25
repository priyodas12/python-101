a,b=23,0

try:
    c=a//b
    print(c) # on exception this will not print
except:
    print("Zero division Error")
finally:
    print("operation completed!")