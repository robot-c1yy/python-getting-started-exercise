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
  