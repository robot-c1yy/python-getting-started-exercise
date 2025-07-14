###第六天###
#if 语句

age =19
if age >=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#if-else语句

age = 17
if age >=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nSorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
    
#if-elif-else 语句

age = 12
if age <4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
    
 #简便式
age = 33
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}")   #elif 可使用多个

###练习### 
    
#练习1
alien_color='green'
if alien_color=='green':
    score=5
elif alien_color=='yellow':
    score=10
elif alien_color=='red':
    score=15
print(f"Congratulations on getting {score} points.")

#使用if 语句处理列表
requested_toppings=['mushroom','green poppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green poppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")        

#确定列表非空

requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
         print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

###练习###
#练习1

name=['admin','qriny','ztiky','poiuy','chuij']
for name_a in name:
    if name_a=='admin':
        print(f"Hello {name_a.title()},would you like to see a status report?")
    elif name==[]:
        print("We need find some users!")
    else:
        print(f"Hello {name_a.title()},thank you for logging in again.")

#练习2

current_users=['robot','n_n','ai_ia','CHY','AHY']
new_users=['robot','CHY','AI_IA','khec','?_?']
current_users_lower=[user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"NO, {new_user} have been used.")
    else:
        print(f"Successful! {new_user}.") 

#练习3

numbers=['1','2','3','4','5','6','7','8','9']
for number in numbers:
    if number=='1':
        print(f"{number}st")
    elif number=='2':
        print(f"\n{number}nd")
    elif number=='3':
        print(f"\n{number}rd")
    else:
        print(f"\n{number}th")