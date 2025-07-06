###第五天###

##if 语句

cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())   #示例

requested_topping='mushrooms'
if requested_topping!='anchovies':
    print("\nHold the anchovies")

age=17
if age != 24:
    print("That's not the correct answer.Please ")

#昨天有事 @__@ ,第二天补上的#
# Sorry my futher #

#and和or的条件测试
age_1=22
age_2=23
print(age_1>=21 and age_2>=21)   #一个条件测试没通过，整个表达式就为False

print(age_1<=6 or age>=8)   #所有条件测试均没有通过，才为False

topping=['qwer','asdf','zxcv','poiu','lkjh','mnbv']
print('qwer' in topping)
print('fhyi' in topping)   #检查某元素是否在列表内

banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish.")

###练习###

#练习1

car='bwm'
print("Is car =='bwm'? I predict True.")
print(car=='bwm')
print("\nIs car=='audi'? I predict False.")
print(car=='audi')

book='novel'
print("\nIs book=='novel'? I predict True.") 
print(book=='novel')
print("\nIs book=='text'?I predict False.")
print(book=='text')

q='a'
print("\nIs q=='a'?I predict True.")
print(q=='a')
print("\nIs q=='s'?I predict False.")
print(q=='s')

z='x'
print("\nIs z=='x'?I predict True.")
print(z=='x')
print("\nIs z=='c'?I predict False.")
print(z=='c')

d='i'
print("\nIs d=='i'?I predict True.")
print(d=='i')
print("\nIs d=='v'?I predict False.")
print(d=='v')

#练习2

str1='apple'
str2='apple'
str3='banana'
print("I predict True:\n",str1==str2)
print("\nI predict False:\n",str1==str3)

text='Hello World'
print("\nI predict True:\n",text.lower()=='hello world')
print("\nI predict False:\n",text.lower()=='hello')




