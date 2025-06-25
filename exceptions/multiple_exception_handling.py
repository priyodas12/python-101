from datetime import datetime

num_list=[3,5,8,1,4,7]
index=0
try:
    index = input("please enter index: ")
    print(f"Printing index: {index} , value: {num_list[int(index)]}")
except ValueError as msg:
    print(f"{msg}: \nindex must be integer, actually we received: {index}")
except IndexError as msg:
    print(f"{msg}: \ninvalid index value entered: {index}")
except Exception as e:
    print(f"Generic Error: {e}")
finally:
    print(f"Executed at: {datetime.today()}")