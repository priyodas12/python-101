from datetime import date

menu_items=input("enter menu_item:price").split(",")
result= {}
menu_length=30
for menu_item in menu_items:
    food_item,price=menu_item.split(":")
    result[food_item]=int(price)

date_length=int(len(str(date.today())))
remaining_length=menu_length-date_length

#print(date_length,type(date_length))

print(f'{'-'*(int(remaining_length/2))}{date.today()}{'-'*(int(remaining_length/2))}')

for food_item in result:
    total_hyphen=menu_length-len(food_item)-len(str(result[food_item]))
    print(f'{food_item}{'-'*total_hyphen}{result[food_item]}')

#input: bread:90,milk:92,wine:560,chicken:221,mutton:883,hotdog:8341,imported_wine:992930