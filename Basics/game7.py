###第三天###
#操作列表
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)   #打印名单中所有名字   for ... in ...
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}.\n")   
    #"\n"使每次循环结束后插入一个空行，将针对各位魔术师的消息编组
print("Everyone ,thank you. That was a great magic show!")   #不需要缩进

###练习###

#练习1
pizzas=['pepperoni','cheese','veggie']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza!")

#练习2
animinals=['dog','cat','rabbit']
for animinal in animinals:
    print(f"A {animinal} would make a great pet.")
print("Any of these animals would make a great pet!")

###创建数值列表###
for value1 in range(1,5): 
    print(value1)   #打印数值列表   range(开始,结束)  注意：结束值不包含在内
    
for value2 in range(6):
    print(value2)   #默认从0开始，结束值不包含在内
    
numbers=list(range(1,6))
print(numbers)   #将数转换为列表

even_numbers=list(range(2,11,2))   #指定步长的数值列表   range(开始,结束,步长)
print(even_numbers)

squares=[]
for value3 in range(1,11):
    square=value3**2   #平方
    squares.append(square)   #将平方添加到列表中
print(squares)   

squares2=[]
for value4 in range(1,9):
    squares.append(value4**2)
print(squares2)   #为了简洁，可不使用临时变量

digits=[1,2,3,4,5,6,7,8,9]
print(max(digits))   #最大值   max()
print(min(digits))   #最小值   min()
print(sum(digits))   #总和   sum()

saquares=[value**2 for value in range(1,11)]
print(saquares)   #列表推导式

###练习###

#练习1
for num in range(1,21):
    print(num)

#练习2
for num2 in range(1,1000001):
    print(num2)

#练习3
num3=list(range(1,1000001)) 
print(max(num3))
print(min(num3))
print(sum(num3))

#练习4
numbers4=list(range(1,21,2))
for numm in numbers4:
    print(numm)

#练习5
numbers5=list(range(3,31,3))
for num5 in numbers5:
    print(num5)
 
#练习6
asdf=[]
for valui in range (1,11):
    asdf.append(valui**3)
print(asdf)
   
#练习7
qwer=[valuu**3 for valuu in range(1,11)]
print(qwer)

###切片###
players=['charles','martina','michael','florence','eli']
print(players[1:3]) #切片 [开始（序数减一）:结束（序数减一）] 注意：结束值不包含在内
print(players[:3])   #从开始到指定位置   [:结束（序数减一）]
print(players[2:])   #从指定位置到末尾   [开始（序数减一）:]
for player in players[:3]:
    print(player.title())   #遍历切片
    
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[ : ]   #切片复制列表
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
my_foods.append('cannoli')   
friend_foods.append('ice cream') 
print("My foods:")
print(my_foods)
print("Friend's foods:")    
print(friend_foods)

###练习###

#练习1
my_foods=['pizza','falafel','carrot cake','chocolate cake','ice cream',
          'cheesecake','pasta']
print("The irst three items in the list are:")
print(my_foods[:3])
print("Three items from the middle of the list are:")
print(my_foods[2:5])
print("The last three items in the list are:")
print(my_foods[-3:])   

#练习2
my_pizzas=['pepperoni','cheese','veggie','hawaiian','bbq chicken','meat lovers']
friend_pizzas=my_pizzas[:]
my_pizzas.append('supreme')
friend_pizzas.append('buffalo chicken')
print("My favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
    
#练习3
print("My favorite foods are:")
for my_food in my_foods:
    print(my_food)




    


    
 

    
    

