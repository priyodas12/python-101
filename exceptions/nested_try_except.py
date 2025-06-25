class NegativeInputError(Exception):
    pass
my_list=[12,324,5,2,14,56]
try:
    try:
        index = input("enter index to print: ")
        result = my_list[int(index)]
    except NegativeInputError as ne:
        print("input cannot be negative: {ne}")
    else:
        print(f"Result: {result}")
except ValueError as ve:
    print(f"ValueError: {ve}")
except BaseException as be:
    print(f"BaseException: {be}")

