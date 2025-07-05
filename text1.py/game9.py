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