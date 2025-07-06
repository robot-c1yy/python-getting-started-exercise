###第四天###

##元组##
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])   #元组也可访问列表元素，但不可修改元素
my_ai=(3,)   #元组是由逗号标识的，必须在元素后面加逗号

for dimension in dimensions:
    print(dimension)   #也可遍历元组所有元素


dimensions=(200,50)
print("Original dimension:")
for dimension in dimensions:
    print(dimension)

dimensions=(400,100)
print("\nModified dimension:")
for dimension  in dimensions:
    print(dimension)   #可修改元组变量

###练习###
foods=('pizzas','noodles','fishs','salad','falafel')
for food in foods:
    print(food)
foods=('pizzas','salad','falafel','sandwich','bread')
print("The foods are changed:")
for food in foods:
    print(food)

#看 PEP 8: https://peps.python.org/pep-0008/



