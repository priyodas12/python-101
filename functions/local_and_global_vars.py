g=9.45 # global variable
print(f"global-1: {g}")

def fun():
    global g
    a=16 # local variable, accessible inside function only
    g=902.839 # modifying global var value, this will alter the value
    print(f"local: {a}, global: {g}")

fun()
print(f"global-2: {g}")

m,n,o='abc',90.93,True

def print_locals():
    a,b,c=3,True,"test"
    print(locals())
    print(globals()) # will also print predefined global var as well

print_locals()