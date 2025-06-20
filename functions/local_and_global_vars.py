g=9.45 # global variable
print(f"global-1: {g}")

def fun():
    global g
    a=16 # local variable, accessible inside function only
    g=902.839 # modifying global var value, this will alter the value
    print(f"local: {a}, global: {g}")

fun()
print(f"global-2: {g}")