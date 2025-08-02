###第九天###
##input()函数的工作原理
message = input("Tell me something, and I will repeat" 
                " it back to you: ")
print(message)

prompt = "If you share your name, we can persionalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name.title()}!")

##int()获取数值输入
age = input("How old are you? ")
age = int(age)
print(age>=18)

#进阶版
height = input("How tall are you, in inches? ")
##注释：1 英尺（inches） = 2.54 厘米
height = int(height)
if height >= 48:
    print("\nYou are tall enough to ride! ")
else:
    print("\nYou'll be able to ride when you're a little older. ")

##求模运算符（%）  指出余数
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
##注释：even 偶数     odd 奇数

##while 循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
##注释：current_number += 1 为 current_number = current_number + 1 简写

##让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
        
##使用标志
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
        
##使用 break 退出循环
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
        
##在循环中使用 continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
#注释：continue 语句让python 忽略余下代码并返回循环的开头
 
##避免无限循环       
##所有练习见gamea.14.py   