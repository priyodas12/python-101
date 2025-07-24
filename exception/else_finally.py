from datetime import datetime

a=input("insert first number: ")
b=input("insert second number: ")

try:
    c=int(a)/int(b)
except Exception as e:
    print(e)
else:
    #python enforces only line can cause exception be part of try
    print(f"result: {float(c)}")
finally:
    print(f"completed at:  {datetime.today()}")